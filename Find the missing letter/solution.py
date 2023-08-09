def find_missing_letter(chars):

    previous = ord(chars[0])
    
    for index in range(1, len(chars)):
        if ord(chars[index]) == previous + 1:
            previous = ord(chars[index])
        else:
            return chr(previous + 1)