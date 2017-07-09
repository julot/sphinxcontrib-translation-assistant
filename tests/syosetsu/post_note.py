from sphinxcontrib.translation_assistant import merge
from sphinxcontrib.translation_assistant.formats import syosetsu

from . import fixtures


def test():
    # No post note
    raw = '\r\n'.join(fixtures.JAPANESE_BODIES)
    translation = '\r\n'.join(fixtures.ENGLISH_BODIES)
    data = merge(raw=raw, translation=translation)
    notes = syosetsu.pluck_post_note(data=data)

    assert [] == notes

    # No post note with pre note
    raw = '\r\n'.join(
        fixtures.JAPANESE['notes']['pre']
        + ['%{}'.format(syosetsu.SEPARATORS[0])]
        + fixtures.JAPANESE_BODIES
    )
    translation = '\r\n'.join(
        fixtures.ENGLISH['notes']['pre']
        + ['']
        + fixtures.ENGLISH_BODIES
    )
    data = merge(raw=raw, translation=translation)
    notes = syosetsu.pluck_post_note(data=data)

    assert [] == notes

    # Expected post note
    post_notes = [
        (
            fixtures.JAPANESE['notes']['post'][0][1:],
            fixtures.ENGLISH['notes']['post'][0],
        ),
        (
            fixtures.JAPANESE['notes']['post'][1][1:],
            fixtures.ENGLISH['notes']['post'][1],
        )
    ]

    # Post note with pre note
    raw = '\r\n'.join(
        fixtures.JAPANESE['notes']['pre']
        + ['%{}'.format(syosetsu.SEPARATORS[0])]
        + fixtures.JAPANESE_BODIES
        + ['%{}'.format(syosetsu.SEPARATORS[0])]
        + fixtures.JAPANESE['notes']['post']
    )
    translation = '\r\n'.join(
        fixtures.ENGLISH['notes']['pre']
        + ['']
        + fixtures.ENGLISH_BODIES
        + ['']
        + fixtures.ENGLISH['notes']['post']
    )
    data = merge(raw=raw, translation=translation)
    notes = syosetsu.pluck_post_note(data=data)

    assert post_notes == notes

    # Post note without pre note
    raw = '\r\n'.join(
        fixtures.JAPANESE_BODIES
        + ['%{}'.format(syosetsu.SEPARATORS[0])]
        + fixtures.JAPANESE['notes']['post']
    )
    translation = '\r\n'.join(
        fixtures.ENGLISH_BODIES
        + ['']
        + fixtures.ENGLISH['notes']['post']
    )
    data = merge(raw=raw, translation=translation)
    notes = syosetsu.pluck_post_note(data=data)

    assert post_notes == notes
