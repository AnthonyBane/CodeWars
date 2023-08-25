def first_non_repeating_letter(s):
    char_count = {}
    for index, char in enumerate(s):
        if char.lower() in char_count:
            char_count[char.lower()].append(index)
        else:
            char_count[char.lower()] = [index]
    return_char = [index for index,char in enumerate(s) if len(char_count[char.lower()]) == 1] 
    return s[return_char[0]] if return_char else ""
        