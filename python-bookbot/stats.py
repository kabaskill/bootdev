def get_num_words(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    normalized_text = text.lower()
    letter_counts = {}

    for letter in normalized_text:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts

def sort_on(item):
    return item["num"]


def dict_sorted_by_value(char_dict):
    sorted_list = []

    for char, count in char_dict.items():
        sorted_list.append({
            "char": char,
            "num": count
        })

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
