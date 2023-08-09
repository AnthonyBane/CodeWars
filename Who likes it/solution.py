def likes(names):
    # your code here
    return_string = ""
    match len(names):
        case 0:
            return_string = "no one likes this"
        case 1:
            return_string = f"{names[0]} likes this"
        case 2:
            return_string = f"{names[0]} and {names[1]} like this"
        case 3:
            return_string = f"{names[0]}, {names[1]} and {names[2]} like this"
        case _:
            return_string = f"{names[0]}, {names[1]} and {len(names) -2} others like this"
            
    return return_string