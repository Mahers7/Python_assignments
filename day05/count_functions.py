def count_characters(content):
    return len(content)

def count_lines(content):
    return content.count('\n') + 1  

def count_words(content):
    return len(content.split())

def count_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            num_chars = count_characters(content)
            num_lines = count_lines(content)
            num_words = count_words(content)
            
            return num_chars, num_lines, num_words
    except FileNotFoundError:
        print("File not found.")
        return None, None, None

