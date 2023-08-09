def duplicate_count(text):
    # Your code goes here
    character_count_dict = {}
    for char in text.lower():
        if char in character_count_dict:
            character_count_dict[char] += 1
        else:
            character_count_dict[char] = 1
    
    return sum(1 for count in character_count_dict.values() if count > 1)