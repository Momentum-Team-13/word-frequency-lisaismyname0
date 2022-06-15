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


def omit_stop_words(dictionary):
    for words in STOP_WORDS:
        print(words)


#omit_stop_words("") 
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
