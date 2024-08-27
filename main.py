"""This is the main file"""


def main():
    """this it the main function for bookbot"""

    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = get_word_count(text)
    book_letter_count = count_chars(text)

    sorted_dict = sort_dict(book_letter_count)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in document")
    print()
    for l in sorted_dict:
        print(f"the '{l}' character was found {book_letter_count[l]} times")
    print("--- End report ---")


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
        if letter.isalpha():
            if letter not in chars_dict:
                chars_dict[letter] = 0
            chars_dict[letter] += 1

    return chars_dict


def sort_dict(d):
    """sort_dict sorts the dictionary by the value, which has to be an int"""

    def key(di):
        """key is a function that is used in the sort function to tell the
        sort function what to sort by"""

        return di["num"]

    # converting dict to list in order to sort
    list_thing = []
    for item in d:
        list_thing.append({"name": item, "num": d[item]})

    list_thing.sort(reverse=True, key=key)

    # converting list back to dictionary in the same format as before
    result_dict = {}
    for i in list_thing:
        letter = i["name"]
        result_dict[letter] = i["num"]

    return result_dict


main()
