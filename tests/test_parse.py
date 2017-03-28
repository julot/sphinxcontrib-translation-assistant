from sphinxcontrib.translation_assistant import split, SEPARATOR


raw_text = '''
%プロローグ
%
%本須　麗乃、22歳。
%　わたしは本が好きだ。
$大好きだ。
%　三度のご飯より愛してる。
%
'''.strip()

english_text = '''
Prologue

　Mototsu Urano, 22 years old.
　I like book.
Very much.
　More than three times meal.
'''.strip()


def test_spli():
    text = '\r\n'.join([raw_text, SEPARATOR, english_text])
    raw, translated = split(text)
    assert raw == [line.strip() for line in raw_text.splitlines()]
    assert translated == [line.strip() for line in english_text.splitlines()]
