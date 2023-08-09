def duplicate_encode(word):
    
    count_dict = {}
    
    for char in word.lower():
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    
    return "".join("(" if count_dict[char] == 1 else ")" for char in word.lower())    