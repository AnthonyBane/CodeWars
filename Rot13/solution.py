def rot13(message):
    
    return_message_list = []
    
    for letter in message:
        char_num = ord(letter)
        
        if ord("A") <= char_num <= ord("Z"):
            starting_position = ord("A")
        elif ord("a") <= char_num <= ord("z"):    
            starting_position = ord("a")
        else:
            return_message_list.append(letter)
            continue
        
        new_alphabet_index = char_num - starting_position + 13
        modded_new_index = new_alphabet_index % 26
        return_message_list.append(chr(modded_new_index + starting_position))
        
    return "".join(return_message_list)