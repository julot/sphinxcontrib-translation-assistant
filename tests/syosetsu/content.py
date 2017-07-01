from sphinxcontrib.translation_assistant import merge
from sphinxcontrib.translation_assistant.formats import syosetsu

from .fixtures import JAPANESE, ENGLISH, JAPANESE_BODIES, ENGLISH_BODIES


def test():
    # Expected result
    contents = [
        (JAPANESE['contents'][0][1:], ENGLISH['contents'][0]),
        (
            ''.join(
                [JAPANESE['contents'][1][1:],
                JAPANESE['contents'][2][1:]],
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
        + ['%{}'.format(syosetsu.SEPARATOR)]
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
        + ['%{}'.format(syosetsu.SEPARATOR)]
        + JAPANESE_BODIES
        + ['%{}'.format(syosetsu.SEPARATOR)]
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
        + ['%{}'.format(syosetsu.SEPARATOR)]
        + JAPANESE['notes']['post']
    )
    translation = '\r\n'.join(
        ENGLISH_BODIES
        + ['']
        + ENGLISH['notes']['post']
    )
    data = merge(raw=raw, translation=translation)
    assert contents == syosetsu.pluck_content(data=data)
