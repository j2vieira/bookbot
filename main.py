def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_dict = sort_dict(chars_dict)
    report(sorted_dict, num_words)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_dict(dict):
    list = []
    for key, value in dict.items():
        if key.isalpha():
            list.append((key, value))

    sorted_list = sorted(list, reverse = True, key = lambda item:item[1])
    return sorted_list

def report(list,num_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")

    for key, value in list:
        print(f"The '{key}' character was found {value} times")

    print("--- End report ---")

main()

