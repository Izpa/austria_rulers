import re

FIRST_URL = 'https://ru.wikipedia.org/wiki/%D0%9B%D0%B5%D0%BE%D0%BF%D0%BE%D0%BB%D1%8C%D0%B4_I_(%D0%BC%D0%B0%D1%80%D0%BA%D0%B3%D1%80%D0%B0%D1%84_%D0%90%D0%B2%D1%81%D1%82%D1%80%D0%B8%D0%B8)'
AUSTRIA_REGEX = 'Австри'
AUSTRIA_PATTERN = re.compile(AUSTRIA_REGEX)

IMPERIAL_REGEX = 'Священной Римской'
IMPERIAL_PATTERN = re.compile(IMPERIAL_REGEX)

SUCCESSOR_REGEX = 'Преемник:'
SUCCESSOR_PATTERN = re.compile(SUCCESSOR_REGEX)

WIKIPEDIA_URL = 'https://ru.wikipedia.org'
