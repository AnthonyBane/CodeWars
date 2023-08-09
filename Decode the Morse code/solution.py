from preloaded import MORSE_CODE

def decode_morse(morse_code):
    
    morse_code += " "
    return_str = ""
    blank_count = 0
    cipher = ""
    
    for char in morse_code:
        if char != " ":
            blank_count = 0
            cipher += char
        else:
            blank_count += 1
            if blank_count == 2:
                return_str += " "
            
            print(cipher)
            if cipher in MORSE_CODE:
                return_str += MORSE_CODE[cipher]
            cipher  = ""
            
    return return_str.strip()