def word_count(book_text):
    book = book_text.split()
    count = 0

    for word in book:
        count += 1
    
    return count

def char_count(book_text):
    chars = {}
    for c in book_text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars