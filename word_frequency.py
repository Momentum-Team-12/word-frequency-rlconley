STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file, 'r') as f:
        # code to read and process the file goes here, where the file is referred to as f.
        # when the indented code block stops, Python will close the file, and f will no longer be defined
        # read() converts the file to a string
        file_string = f.read()
        # splitlines() will return a list with each element being a line in the file
        file_list = file_string.splitlines()
        # strip() and split() can also be helpful in this process.

# this will print out one line at a time
    for line in file_list:   
        print(line)


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
