from pydoc import text


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    print(f"Your file is: {file}")
    with open(file) as open_file:
        read_file = open_file.read()
    for word in STOP_WORDS:
        if word in read_file:
            read_file = read_file.replace(f"{word}", "")
    print(read_file)
    # omit stop words around here
    """lowercase = read_file.lower()
    lowercase_without_periods = lowercase.replace(".", "")
    lowercase_without_commas = lowercase_without_periods.replace(",", "")
    lowercase_without_question = lowercase_without_commas.replace("?", "")
    lowercase_no_hyphen = lowercase_without_question.replace(
        "-", " ")
    text_split = lowercase_no_hyphen.split()
    text_dictionary = dict.fromkeys(text_split, 0)
    print(text_dictionary)
    for word in text_split:
        text_dictionary[word] += 1
    print(text_dictionary)"""


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

#omit_stop_words(" ")
