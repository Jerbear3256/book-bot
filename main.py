from stats import *
import sys

def get_book_text(file:str):
    with open(file) as f:
        contents = f.read()
    return contents

def print_report(file:str,wordCount:int,characterCount:list[tuple[str,int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {wordCount} total words")
    print("--------- Character Count -------")
    for charTuple in characterCount:
        if charTuple[0].isalpha():
            print(f"{charTuple[0]}: {charTuple[1]}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = sys.argv[1]
    text = get_book_text(file)
    wordCount = word_count(text)
    characterCount = chars_dict_to_sorted_list(char_count(text))
    # print(f"Found {wordCount} total words")
    # print(characterCount)
    print_report(file,wordCount,characterCount)


main()