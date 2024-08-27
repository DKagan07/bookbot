"""This is the main file"""


def main():
    """this it the main function for bookbot"""

    text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(text)
    print(word_count)

    book_letter_count = count_chars(text)
    print(book_letter_count)


def get_book_text(path):
    """get_book_text returns the text of a book"""
    with open(path, encoding="UTF-8") as f:
        return f.read()


def get_word_count(s):
    """get_word_count gets the word count for a string"""
    words = s.split()
    return len(words)


def count_chars(s):
    """count_chars counts how many characters there are in a string
    of note, this does not distinguish between upper case and lower case
    letters"""

    chars_dict = {}

    for letter in s:
        letter = letter.lower()
        if letter not in chars_dict:
            chars_dict[letter] = 0
        chars_dict[letter] += 1

    return chars_dict


main()
