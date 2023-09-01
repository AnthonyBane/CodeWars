def count(s):
    character_count_dict = {}
    for char in s:
        if char in character_count_dict:
            character_count_dict[char] += 1
        else:
            character_count_dict[char] = 1

    return character_count_dict


def count_v2(s):
    character_count_dict = {}
    for char in s:
        character_count_dict[char] = character_count_dict.get(char, 0) + 1

    return character_count_dict
