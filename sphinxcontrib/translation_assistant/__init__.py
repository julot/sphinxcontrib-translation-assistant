from collections import deque
from itertools import zip_longest
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive as BaseDirective

from sphinxcontrib.translation_assistant.formats import syosetsu


SEPARATOR = '---SEPERATOR---'


def merge(raw, translation):
    """
    Merge raw and translation into deque of tuple(raw, translation).

    Also merge two lines of paragraph into one.

    :param raw: Raw text.
    :param translation: Translation text.
    :return: Return deque of tuple(raw, translation)

    :type raw: str
    :type translation: str
    :rtype: Iterable

    """

    data = deque()
    raws = raw.splitlines()
    translations = translation.splitlines()

    for raw, translation in zip_longest(raws, translations, fillvalue=''):
        if not raw:
            continue

        prefix = raw[0]
        raw = raw[1:]
        if prefix == '$':
            prev_raw, prev_translation = data.pop()
            raw = ''.join([prev_raw, raw])
            translation = ' '.join([prev_translation, translation])

        data.append((raw, translation))

    return data


def progress(data):
    """
    Calculate translation progress.

    :param data: Result from merge function.
    :return: Return float between 0 and 1.

    :type data: Iterable
    :rtype: float

    """

    raw = sum(1 for i, _ in data if i)
    translation = sum(1 for _, i in data if i)
    return raw / translation


class Directive(BaseDirective):

    required_arguments = 1  # Path to translation assistant file
    final_argument_whitespace = True
    has_content = False

    @staticmethod
    def paragraphs(raw, translation):
        """
        Create raw and translation paragraph.

        :param raw: Raw text
        :param translation: Translation text
        :return: list of paragraph node.

        :type raw: str
        :type translation: str
        :rtype: iterable

        """
        if not raw:
            yield nodes.paragraph(classes=['break'], text='\u3000')
            return

        yield nodes.paragraph(classes=['raw'], text=raw)

        # If raw is empty, put more blank lines to emphasis section break.
        # if not raw:
        #     yield nodes.paragraph(classes=['translated'], text='\u3000')
        #     return

        # Only add translation paragraph if the text is not empty.
        if translation.strip():
            yield nodes.paragraph(classes=['translated'], text=translation)

    def run(self):
        env = self.state.document.settings.env

        rel_path, path = env.relfn2path(directives.path(self.arguments[0]))
        env.note_dependency(rel_path)

        with open(path, encoding='utf-8') as f:
            text = f.read()

        if text[0] != '\ufeff':
            raise ValueError('Not a valid Translation Assistant format.')

        raw, translation = text[1:].split(SEPARATOR)

        data = merge(raw=raw.strip(), translation=translation.strip())

        titles = syosetsu.pluck_title(data=data)
        pre_notes = syosetsu.pluck_pre_note(data=data)
        contents = syosetsu.pluck_content(data=data)
        post_notes = syosetsu.pluck_post_note(data=data)

        title = ' \u30fc '.join(titles)
        section = nodes.section(ids=title)
        section.append(nodes.title(text=title))

        if pre_notes:
            for raw, translation in pre_notes:
                paragraphs = self.paragraphs(raw=raw, translation=translation)
                section.extend(paragraphs)
            section.append(nodes.transition())

        for raw, translation in contents:
            section.extend(self.paragraphs(raw=raw, translation=translation))

        if post_notes:
            section.append(nodes.transition())
            for raw, translation in post_notes:
                paragraphs = self.paragraphs(raw=raw, translation=translation)
                section.extend(paragraphs)

        return [section]


def setup(app):
    app.add_directive('translation-assistant', Directive)
