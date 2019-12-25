import xml.etree.ElementTree as ET
from collections import Counter

words_counter = Counter()
non_alphabetical_words = Counter()
defect_words_counter = Counter()


def all_words():
    print(len(words_counter))
    print('All words counter:')
    for word in words_counter.most_common():
        print(word)
    print('\n' * 4)


def words_with_non_alphabetical_symbols():
    print('Words with non-alphabetical symbols:')
    for word in non_alphabetical_words.most_common():
        print(word)
    print('\n' * 4)


def defect_words():
    print('Defect words:')
    for word in defect_words_counter.most_common():
        symbols_ord = ' '.join([str(ord(s)) for s in word[0]])
        print(f'{word}                {symbols_ord}')
    print('\n' * 4)


def not_classified_words():
    print('Not classified words:')
    for word in words_counter.most_common():
        if not word[0][0].isalpha() or not word[0][-1].isalpha():
            print(word)
    print('\n' * 4)


if __name__ == "__main__":
    tree = ET.parse('Шабанова - Одной дорогой.fb2')
    root = tree.getroot()

    for paragraph in root.iter('{http://www.gribuser.ru/xml/fictionbook/2.0}p'):
        if paragraph.text:
            split_text = paragraph.text.split()
            words = [word.strip(''',.…!«»?-–—'"():;„“''') for word in split_text]
            for word in words:
                if word:
                    if word.count('-') < 3 and not any(
                            not (1040 <= ord(symbol) <= 1103 or ord(symbol) in [45, 1025, 1105]) for symbol in word):
                        if word.isalpha():
                            words_counter[word.lower()] += 1
                        else:
                            non_alphabetical_words[word.lower()] += 1
                    elif not word.isdigit() and any(
                            1040 <= ord(symbol) <= 1103 or ord(symbol) in [1025, 1105] for symbol in word):
                        defect_words_counter[word.lower()] += 1
    all_words()
    words_with_non_alphabetical_symbols()
    defect_words()
    not_classified_words()
