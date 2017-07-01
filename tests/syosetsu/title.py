from sphinxcontrib.translation_assistant import merge
from sphinxcontrib.translation_assistant.formats import syosetsu

from . import fixtures


def test():
    raw = '\r\n'.join(fixtures.JAPANESE_BODIES)
    translation = '\r\n'.join(fixtures.ENGLISH_BODIES)
    data = merge(raw=raw, translation=translation)
    titles = syosetsu.pluck_title(data=data)

    assert fixtures.TITLES == titles

    raw = '\r\n'.join(
        fixtures.JAPANESE['notes']['pre']
        + [syosetsu.SEPARATOR]
        + fixtures.JAPANESE_BODIES
    )
    translation = '\r\n'.join(
        fixtures.ENGLISH['notes']['pre']
        + ['']
        + fixtures.ENGLISH_BODIES
    )
    data = merge(raw=raw, translation=translation)
    titles = syosetsu.pluck_title(data=data)

    assert fixtures.TITLES == titles
