import xml.etree.ElementTree as ET
from collections import Counter
from string import punctuation

words_counter = Counter()
wrong_words = []


def all_words():
    print(len(words_counter))
    print('All words counter:')
    for word in words_counter.most_common():
        print(word)
    print('\n' * 4)


def words_with_non_alphabetical_symbols():
    print('Words with non-alphabetical symbols:')
    for word in words_counter.most_common():
        if not word[0].isalpha():
            print(word)
    print('\n' * 4)


def defect_words():
    print('Defect words:')
    for word in wrong_words:
        symbols_ord = ' '.join([str(ord(s)) for s in word])
        print(f'{word}                {symbols_ord}')
    print('\n' * 4)


def not_classified_words():
    print('Not classified words:')
    for word in words_counter.most_common():
        if not word[0][0].isalpha() or not word[0][-1].isalpha():
            print(word)
    print('\n' * 4)


if __name__ == "__main__":
    tree = ET.parse('Fuchs - Продавец специй.fb2')
    root = tree.getroot()

    for paragraph in root.iter('{http://www.gribuser.ru/xml/fictionbook/2.0}p'):
        if paragraph.text:
            split_text = paragraph.text.split()
            words = [word.strip(punctuation).strip(',.…!«»?-–—1234567890()') for word in split_text]
            for word in words:
                if word and word.count('-') < 3 and not any(
                        not (1040 <= ord(symbol) <= 1103 or ord(symbol) in [45, 1025, 1105]) for symbol in word):
                    words_counter[word.lower()] += 1
                elif word:
                    wrong_words.append(word.lower())
    all_words()
    words_with_non_alphabetical_symbols()
    defect_words()
    not_classified_words()
