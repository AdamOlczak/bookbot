def report(book_name):
    book = __get_book(book_name)
    words = __count_words(book)
    chars = __count_characters(book)
    print(f"--- Begin report of books/{book_name} ---")
    print(f"{words} found in the document")
    print()
    for c in chars:
        if not c.isalpha():
            continue
        print(f"The '{c}' character was found {chars[c]} times")
    print("--- End report ---")


def __get_book(book):
    with open(f"books/{book}") as f:
        return f.read()


def __count_words(text):
    return len(text.split())


def __count_characters(text):
    chars = {}
    for c in text:
        c = c.lower()
        chars[c] = chars.get(c, 0) + 1
    return chars
