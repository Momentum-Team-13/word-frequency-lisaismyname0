from pydoc import text
from re import A


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    print(f"Your file is: {file}")
    with open(file) as open_file:
        read_file = open_file.read()
    new_file = []
    ommited_words = []

    for word in STOP_WORDS:
        word = word.split('\n')
        ommited_words.append(word[0])
        print(word)
    for word in read_file:
        print(word)
    print(new_file)
    print(ommited_words)
    p = [t for t in new_file if t not in STOP_WORDS]
    print(type(p))
    # omit stop words around here
    lowercase = read_file.lower()
    lowercase_without_punct1 = lowercase.replace(".", "").replace(",", "")
    lowercase_without_punct = lowercase_without_punct1.replace(
        "?", "").replace("-", "")
    text_split = lowercase_without_punct.split()

    text_dictionary = dict.fromkeys(text_split, 0)
    for word in text_split:
        text_dictionary[word] += 1
    alphabetized = dict(sorted(text_dictionary.items()))
    return alphabetized


"""    words = text_dictionary.keys()
    print(words)
    frequency = text_dictionary.values()
    print(frequency)"""


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

# omit_stop_words(" ")

"""    for word in read_file:
        if word in STOP_WORDS:
            read_file = read_file.replace(word, "")"""
