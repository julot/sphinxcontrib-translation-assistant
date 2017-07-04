JAPANESE = {
    'title': '%プロローグ',
    'contents': [
        '%　｜本須　麗乃（もとすうらの）、22歳。',
        '%　わたしは本が好きだ。',
        '$大好きだ。',
        '%　三度のご飯より愛してる。',
        '%「うっ……」',
    ],
    'notes': {
        'pre': [
           '%蒼枝と申します。',
           '%長編を書くのは初めてです。',
        ],
        'post': [
            '%とうとう始めてしまいました。',
            '%楽しんでいただけたら嬉しいです。',
        ],
    },
}

ENGLISH = {
    'title': 'Prologue',
    'contents': [
        '　My name is Mototsu Urano, 22 years old.',
        '　I like book.',
        'Really really like.',
        '　I love it more than three times meals.',
        '「Uu……」'
    ],
    'notes': {
        'pre': [
            'I am Aoieda.',
            "It's my first time writing novel.",
        ],
        'post': [
            'It has started at last.',
            'I am glad if you enjoy it.',
        ],
    },
}

JAPANESE_BODIES = [
    JAPANESE['title'],
    '%',
    JAPANESE['contents'][0],
    JAPANESE['contents'][1],
    JAPANESE['contents'][2],
    JAPANESE['contents'][3],
]

ENGLISH_BODIES = [
    ENGLISH['title'],
    '',
    ENGLISH['contents'][0],
    ENGLISH['contents'][1],
    ENGLISH['contents'][2],
    ENGLISH['contents'][3],
]

TITLES = (JAPANESE['title'][1:], ENGLISH['title'])
