import string


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    input_str = open_file(file)
    """Read in `file` and print out the frequency of words in that file."""
    punctuation = string.punctuation
    new_str = input_str
    print(input_str)
    for char in input_str:
        if char in punctuation:
            new_str = new_str.replace(char, "")
    print(new_str)
    print(new_str.lower())
    new_str = new_str.lower()
    list_of_words = new_str.split()
    print(list_of_words)
    list_of_words = [word for word in new_str if new_str not in STOP_WORDS]
    result = ''.join(list_of_words)
    print(result)

# new_words = []
# for word in words:
#     if word not in STOP_WORDS:
#         new_words.append(word)

def open_file(file):
    with open(file) as file:
        open_file = file.read()
        print(open_file)
    return open_file
    # pass


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
