import logging

from sphinxcontrib.translation_assistant import merge
from sphinxcontrib.translation_assistant.formats import syosetsu

from . import fixtures


def test():
    print('Test Pre Note')
    logger = logging.getLogger(
        'sphinxcontrib.translation_assistant.formats.syosetsu'
    )
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

    raw = '\r\n'.join(fixtures.JAPANESE_BODIES)
    translation = '\r\n'.join(fixtures.ENGLISH_BODIES)
    data = merge(raw=raw, translation=translation)
    notes = syosetsu.pluck_pre_note(data=data)

    assert [] == notes

    raw = '\r\n'.join(
        fixtures.JAPANESE['notes']['pre']
        + ['%{}'.format(syosetsu.SEPARATOR)]
        + fixtures.JAPANESE_BODIES
    )
    translation = '\r\n'.join(
        fixtures.ENGLISH['notes']['pre']
        + ['']
        + fixtures.ENGLISH_BODIES
    )
    data = merge(raw=raw, translation=translation)
    notes = syosetsu.pluck_pre_note(data=data)

    result = [
        (
            fixtures.JAPANESE['notes']['pre'][0][1:],
            fixtures.ENGLISH['notes']['pre'][0],
        ),
        (
            fixtures.JAPANESE['notes']['pre'][1][1:],
            fixtures.ENGLISH['notes']['pre'][1],
        )
    ]
    assert result == notes
