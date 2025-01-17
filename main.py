def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as file:
        file_contents = file.read()

    print_book_data(file_contents, path_to_file)

def count_words(file_contents):
    return len(file_contents.split())

def count_chars(file_contents):

    char_dict = {}

    for chars in file_contents:

        if chars.isalpha() == False:
            continue

        lc_char = chars.lower()

        if lc_char in char_dict:
            char_dict[lc_char] += 1
        else:
            char_dict[lc_char] = 1

    return char_dict

def print_book_data(file_contents, path_to_file):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{count_words(file_contents)} words found in the document\n")

    char_dict = count_chars(file_contents)

    for char, count in char_dict.items():
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

main()
