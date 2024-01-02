import sys


def report(filepath):
    try:
        book = __get_book(filepath)
    except FileNotFoundError:
        print(f'File "{filepath}" has not been found.', file=sys.stderr)
        return
    words = __count_words(book)
    chars = __count_characters(book)
    print(f"--- Begin report for {filepath} ---")
    print(f"{words} word(s) have been found in the document")
    for c in chars:
        if not c.isalpha():
            continue
        print(f"The '{c}' character has been found {chars[c]} times")
    else:
        print("No characters have been found in the document")
    print("--- End report ---")


def __get_book(filepath):
    with open(f"{filepath}") as f:
        return f.read()


def __count_words(text):
    return len(text.split())


def __count_characters(text):
    chars = {}
    for c in text:
        c = c.lower()
        chars[c] = chars.get(c, 0) + 1
    return chars
