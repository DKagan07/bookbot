"""This is the main file"""


def main():
    """this it the main function for bookbot"""

    text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(text)
    print(word_count)


def get_book_text(path):
    """get_book_text returns the text of a book"""
    with open(path, encoding="UTF-8") as f:
        return f.read()


def get_word_count(s):
    """get_word_count gets the word count for a string"""
    words = s.split()
    return len(words)


main()
