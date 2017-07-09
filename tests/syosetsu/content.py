from sphinxcontrib.translation_assistant import merge
from sphinxcontrib.translation_assistant.formats import syosetsu

from .fixtures import JAPANESE, ENGLISH, JAPANESE_BODIES, ENGLISH_BODIES


def test():
    # Without notes started with 「
    contents = [
        (JAPANESE['contents'][4][1:], ENGLISH['contents'][4]),
        (JAPANESE['contents'][0][1:], ENGLISH['contents'][0]),
        (
            ''.join(
                [JAPANESE['contents'][1][1:], JAPANESE['contents'][2][1:]],
            ),
            ' '.join([ENGLISH['contents'][1], ENGLISH['contents'][2]]),
        ),
        (JAPANESE['contents'][3][1:], ENGLISH['contents'][3]),
    ]
    japanese_bodies = [
        JAPANESE['title'],
        '%',
        JAPANESE['contents'][4],
        JAPANESE['contents'][0],
        JAPANESE['contents'][1],
        JAPANESE['contents'][2],
        JAPANESE['contents'][3],
    ]
    raw = '\r\n'.join(japanese_bodies)
    english_bodies = [
        ENGLISH['title'],
        '',
        ENGLISH['contents'][4],
        ENGLISH['contents'][0],
        ENGLISH['contents'][1],
        ENGLISH['contents'][2],
        ENGLISH['contents'][3],
    ]
    translation = '\r\n'.join(english_bodies)
    data = merge(raw=raw, translation=translation)
    assert contents == syosetsu.pluck_content(data=data)

    # Expected result
    contents = [
        (JAPANESE['contents'][0][1:], ENGLISH['contents'][0]),
        (
            ''.join(
                [JAPANESE['contents'][1][1:], JAPANESE['contents'][2][1:]],
            ),
            ' '.join([ENGLISH['contents'][1], ENGLISH['contents'][2]]),
        ),
        (JAPANESE['contents'][3][1:], ENGLISH['contents'][3]),
    ]

    # Without notes
    raw = '\r\n'.join(JAPANESE_BODIES)
    translation = '\r\n'.join(ENGLISH_BODIES)
    data = merge(raw=raw, translation=translation)
    assert contents == syosetsu.pluck_content(data=data)

    # Pre note only
    raw = '\r\n'.join(
        JAPANESE['notes']['pre']
        + ['%{}'.format(syosetsu.SEPARATORS[0])]
        + JAPANESE_BODIES
    )
    translation = '\r\n'.join(
        ENGLISH['notes']['pre']
        + ['']
        + ENGLISH_BODIES
    )
    data = merge(raw=raw, translation=translation)
    assert contents == syosetsu.pluck_content(data=data)

    # With post note and pre note
    raw = '\r\n'.join(
        JAPANESE['notes']['pre']
        + ['%{}'.format(syosetsu.SEPARATORS[0])]
        + JAPANESE_BODIES
        + ['%{}'.format(syosetsu.SEPARATORS[0])]
        + JAPANESE['notes']['post']
    )
    translation = '\r\n'.join(
        ENGLISH['notes']['pre']
        + ['']
        + ENGLISH_BODIES
        + ['']
        + ENGLISH['notes']['post']
    )
    data = merge(raw=raw, translation=translation)
    assert contents == syosetsu.pluck_content(data=data)

    # Post note without pre note
    raw = '\r\n'.join(
        JAPANESE_BODIES
        + ['%{}'.format(syosetsu.SEPARATORS[0])]
        + JAPANESE['notes']['post']
    )
    translation = '\r\n'.join(
        ENGLISH_BODIES
        + ['']
        + ENGLISH['notes']['post']
    )
    data = merge(raw=raw, translation=translation)
    assert contents == syosetsu.pluck_content(data=data)
