def expanded_form(num):
    return_string = ""
    for index, char in enumerate(str(num), start = 1):
        if char != "0":
            if len(return_string) > 0:
                return_string += " + "
            return_string += (char) + ("0"*(len(str(num)) - index))
            
    return return_string

