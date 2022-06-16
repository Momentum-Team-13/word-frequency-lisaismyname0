from pydoc import text


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    print(f"Your file is: {file}")
    with open(file) as open_file:
        read_file = open_file.readlines()
    # print(read_file)
    file_as_string = str("".join(read_file))
    str(file_as_string.replace(",", " "))
    print(file_as_string)
    print(type(read_file))
    print(type(file_as_string))
    print(len(file_as_string))
    lowercase = file_as_string.lower()
    print(lowercase)
    lowercase_without_periods = lowercase.replace(".", "")
    print(lowercase_without_periods)
    lowercase_without_commas = lowercase_without_periods.replace(",", "")
    print(lowercase_without_commas)
    lowercase_without_question = lowercase_without_commas.replace("?", "")
    print(lowercase_without_question)
    lowercase_no_hyphen = lowercase_without_question.replace(
        "-", " ")
    print(lowercase_no_hyphen)
    lowercase_no_apostrophe = lowercase_no_hyphen.replace("'", " ")
    print(lowercase_no_apostrophe)
    text_split = lowercase_no_apostrophe.split(" ")
    print(text_split)
    text_dictionary = dict.fromkeys(text_split, "0")
    print(text_dictionary)
    for key in text_dictionary:
        if f"{key}" == f"{key}":
            print("got a double! with :" f"{key}" f"{key}")


def omit_stop_words(dictionary):
    for words in STOP_WORDS:
        print(words)


# omit_stop_words("")
# why does calling this here print the words at the top of the console?

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
