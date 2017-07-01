from sphinxcontrib.translation_assistant import merge
from tests.syosetsu import fixtures


def test():
    raw = '\r\n'.join(fixtures.JAPANESE_BODIES)
    translation = '\r\n'.join(fixtures.ENGLISH_BODIES)
    data = merge(raw=raw, translation=translation)

    assert data[0][0] == fixtures.JAPANESE_BODIES[0][1:]
    assert data[0][1] == fixtures.ENGLISH_BODIES[0]
