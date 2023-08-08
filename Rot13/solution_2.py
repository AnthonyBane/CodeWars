def rot13(message):
    
    return_message_list = []
    
    for letter in message:
        char_num = ord(letter)
        
        if 65 <= char_num <= 90:
            starting_position = 65
        elif 97 <= char_num <= 122:    
            starting_position = 97
        else:
            return_message_list.append(letter)
            continue
        
        new_alphabet_index = char_num - starting_position + 13
        modded_new_index = new_alphabet_index % 26
        return_message_list.append(chr(modded_new_index + starting_position))
        
    return "".join(return_message_list)