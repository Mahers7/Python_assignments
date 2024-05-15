import sys

def count_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            charachters = len(content)
            lines = content.count('\n') + 1 
            words = len(content.split())
            
            print(f"Number of characters: {charachters}")
            print(f"Number of lines: {lines}")
            print(f"Number of words: {words}")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count.py FILENAME")
    else:
        count_file(sys.argv[1])
