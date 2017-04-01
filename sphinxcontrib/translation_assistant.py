from collections import deque
from itertools import zip_longest
from docutils import nodes
from docutils.statemachine import ViewList
from docutils.parsers.rst import directives

from sphinx.util.compat import Directive as BaseDirective


SEPARATOR = '---SEPERATOR---'


def parse(text):
    if text[0].encode() != b'\xef\xbb\xbf':
        raise ValueError('Not a valid Translation Assistant format.')

    return merge(*split(text=text[1:]))


def split(text):
    texts = text.split(SEPARATOR)
    raws = [line.strip() for line in texts[0].strip().splitlines()]
    translations = [line.rstrip() for line in texts[1].strip().splitlines()]

    return raws, translations


def merge(raws, translations):
    data = deque()

    for raw, translation in zip_longest(raws, translations, fillvalue=''):
        prefix = raw[0]
        if prefix == '$':
            previous = len(data) - 1
            data[previous][0] = ''.join([data[previous][0], raw[1:]])
            data[previous][1] = ' '.join([data[previous][1], translation])
        else:
            data.append([raw[1:], translation])

    return data


class Directive(BaseDirective):

    required_arguments = 1  # Path to yml file
    final_argument_whitespace = True
    has_content = False

    option_spec = {
        'no-title': directives.flag,
        'no-raw': directives.flag,
    }

    def run(self):
        env = self.state.document.settings.env

        rel_path, path = env.relfn2path(directives.path(self.arguments[0]))
        env.note_dependency(rel_path)

        no_title = 'no-title' in self.options
        no_raw = 'no-raw' in self.options

        with open(path, encoding='utf-8') as f:
            text = f.read()

        lines = parse(text=text)

        section = None

        if not no_title:
            line = lines.popleft()
            if no_raw:
               title = line[1]
            else:
                title = '{0} ー {1}'.format(line[0], line[1])
            section = nodes.section(ids=title)
            section.append(nodes.title(text=title))
            lines.popleft()

        contents = []

        for line in lines:
            if not line[0].strip():
                contents.append(nodes.paragraph(classes=['blank'], text='　'))
                continue

            if line[0].strip()[:4] == '----':
                contents.append(nodes.transition())
                continue

            if not no_raw:
                paragraph = nodes.paragraph(classes=['raw'], text=line[0])
                contents.append(paragraph)

            if line[1].strip():
                paragraph = nodes.paragraph(
                    classes=['translated'],
                    text=line[1],
                )
                contents.append(paragraph)

        if not no_title:
            section.extend(contents)

        return [section] if section else contents


def setup(app):
    app.add_directive('translation-assistant', Directive)
