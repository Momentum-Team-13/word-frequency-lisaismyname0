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
    text_split = lowercase_without_punct.split()
    screened_words = [word for word in text_split if word not in STOP_WORDS]
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

"""anonymous functions are not named functions bc they are small and happen in particular circumstances. so key = lambda is an anonymous function like eventlisters and the e variables in javascript, lambda takes x and returns the first value from whatever x is. mostly comes up as a key while working on dictionaries"""
