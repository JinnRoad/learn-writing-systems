from itertools import permutations
from random import choice


file = 'writing-systems/jp-hiragana.txt'  # TSV containing glyphs and romanization
test_order = 0  # Test glyph first: 0. Test romanization first: 1
glyphs_per_word = 2

def main():
    syllables = load_tsv(file)
    question, answer = (0, 1) if not test_order else (1, 0)
    while True:
        word = make_word(syllables, glyphs_per_word)
        input(word[question])
        print(word[answer])
        print()

def load_tsv(file):
    """Load TSV into tuple"""
    with open(file, 'r', encoding='utf-8') as file:
        rows = tuple(tuple(line.strip().split()) for line in file)
    return rows

def make_word(syllables, length):
    glyphs = []
    romanizations = []
    for _ in range(length):
        glyph, romanization = choice(syllables)
        glyphs.append(glyph)
        romanizations.append(romanization)
    return (''.join(glyphs), ''.join(romanizations))


main()
