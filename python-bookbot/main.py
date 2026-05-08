import sys
from stats import get_num_words
from stats import get_letter_count
from stats import dict_sorted_by_value

def main():

    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    letters = get_letter_count(text)
    sorted_letters = dict_sorted_by_value(letters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")

    for item in sorted_letters:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def get_book_text(arg):
    with open(arg) as f:
        file_contents = f.read()
        return file_contents

main()


