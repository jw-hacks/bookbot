import sys
from stats import get_num_words, character_count, sort_character_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def format_report(book_path, book_word_count, sorted_dict):
    character_report = "\n".join([f"{char}: {count}" for char, count in sorted_dict.items()])
    print(f"""
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {book_word_count} total words
--------- Character Count -------
{character_report}
============= END ===============
""")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    book_word_count = get_num_words(book_text)
    #print(f"{book_word_count} words found in the document")
    character_dict = character_count(book_text)
    #print(character_dict)
    sorted_dict = sort_character_dict(character_dict)
    format_report(book_path, book_word_count, sorted_dict)

main()