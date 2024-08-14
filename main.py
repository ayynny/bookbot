def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    get_char_count(text)
   
    print(f"--- End report ---")




def get_num_words(text):
    words = text.split() 
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text): 
    lowered_string = text.lower()
    
    char_counts = {}

    for character in range(0,len(lowered_string)):
        if char_counts.get(lowered_string[character]) == None:
            char_counts.update({lowered_string[character]:1})
        else:
            char_counts[lowered_string[character]] += 1

    for key,val in char_counts.items():
        if key.isalpha() == True:
            print(f"The '{key}' character was found {val} times")

main()