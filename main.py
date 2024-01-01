def __get_book(book):
    with open(f"books/{book}") as f:
        return f.read()

def __count_words(text):
    return len(text.split())

def __count_letters(text):
    letters = {}
    for c in text:
        if not c.isalpha():
            continue
        c = c.lower()
        letters[c] = letters.get(c, 0) + 1
    return letters

def report(book_name):
    book = __get_book(book_name)
    words = __count_words(book)
    letters = __count_letters(book)
    print(f"--- Begin report of books/{book_name} ---")
    print(f"{words} found in the document")
    print()
    for letter in letters:
        print(f"The '{letter}' character was found {letters[letter]} times")
    print("--- End report ---")

def main():
    report("frankenstein.txt")

if __name__ == "__main__":
    main()
