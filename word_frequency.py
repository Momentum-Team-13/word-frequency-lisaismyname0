from pydoc import text
# call file in terminal by entering:
# > ❯ python word_frequency.py praise_song_for_the_day.txt

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with',
]


def print_word_freq(file):
    print(f"Your file is: {file}")
    with open(file) as open_file:
        read_file = open_file.read()
    lowercase = read_file.lower()
    lowercase_without_punct1 = lowercase.replace(".", "").replace(",", "")
    lowercase_without_punct = lowercase_without_punct1.replace(
        "?", "").replace("'", "")
    ommited_words = []
    screened_words = []
    text_split = lowercase_without_punct.split()
    for word in text_split:
        if word in STOP_WORDS:
            ommited_words.append(word)
        if word not in STOP_WORDS:
            screened_words.append(word)
    text_dictionary = dict.fromkeys(screened_words, 0)
    for word in screened_words:
        text_dictionary[word] += 1
    alphabetized = dict(sorted(text_dictionary.items()))
    for key, value in alphabetized.items():
        print(key, "|", value, "*"*value)


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
