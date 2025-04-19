def get_num_words(book_text):
    word_list = book_text.split()
    word_count = len(word_list)
    return word_count

def character_count(book_text):
    character_list = list(book_text.lower())
    char_dict = {}
    for char in character_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict            

def sort_character_dict(char_dict):
    filtered_dict = {k: v for k, v in char_dict.items() if k.isalpha()}
    sorted_dict = dict(sorted(filtered_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict
