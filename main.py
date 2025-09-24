from stats import word_count
from stats import char_count

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

def main():
    book = get_book_text("./books/frankenstein.txt")
    count = word_count(book)
    print(f"Found {count} total words")
    print(char_count(book))

main()

