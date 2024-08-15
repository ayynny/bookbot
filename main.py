def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print("--- Begin report of books/frankenstein.txt ---")
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document\n")

    chars_dict = get_chars_dict(text)
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict[""]


def get_chars_dict(text):
    chars = {}
    lowered_text = text.lower()

    for char in lowered_text:
        if char.isalpha() == True:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

    sorted_chars = sorted(chars.items(), key=lambda item: item[1], reverse=True)


    for key, value in sorted_chars:
        print(f"The {key} character was found {value} times")
    #return chars


    


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
