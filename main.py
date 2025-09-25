from stats import word_count
from stats import char_count
from stats import sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

def main():
    book = get_book_text("./books/frankenstein.txt")
    wcount = word_count(book)
    ccount = char_count(book)
    sort_count = sort_chars(ccount)

    print("============ BOOKBOT ============")
    print("Analyzing book found at /books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {wcount} total words")
    print("-------- Character Count --------")
    for c in sort_count:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")

main()

