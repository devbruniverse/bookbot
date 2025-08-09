def get_book_words_count(text):
    words_count = text.split()

    return len(words_count)

def get_book_characters_count(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def sort_characters_count(char_dict):
    char_list = []
    
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    char_list.sort(key = lambda x: x["num"], reverse = True)
    
    return char_list