def unique_in_order(sequence):
    if len(sequence) == 0:
        return []
    return_sequence = [sequence[0]]
    last_character = sequence[0]
    for character in sequence[1:]:
        if last_character != character:
            return_sequence.append(character)
        last_character = character
    
    return return_sequence