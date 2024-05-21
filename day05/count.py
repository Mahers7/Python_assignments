import sys
from count_functions import count_file_contents

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count.py FILENAME")
    else:
        filename = sys.argv[1]
        num_chars, num_lines, num_words = count_file_contents(filename)
        if num_chars is not None:
            print(f"Number of characters: {num_chars}")
            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")