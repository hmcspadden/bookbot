import sys
from stats import word_count
from stats import char_count
from stats import sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

def has_book():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    has_book()
    book = get_book_text(sys.argv[1])
    wcount = word_count(book)
    ccount = char_count(book)
    sort_count = sort_chars(ccount)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {wcount} total words")
    print("-------- Character Count --------")
    for c in sort_count:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")

main()

