
def word_count(text:str):
    words = text.split()
    return len(words)

def char_count(text:dict[str,int]):
    chars = {}
    for char in text.lower():
        # iterate through every character and increase its value in chars
        # make the character's value 1 if it is not already in chars
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def sort_on(char:tuple[str,int]):
    return char[1]

def chars_dict_to_sorted_list(chars:dict[str,int]):
    lst = [(key,value) for key,value in chars.items()]
    sortedList = sorted(lst, key=sort_on, reverse=True)
    return sortedList