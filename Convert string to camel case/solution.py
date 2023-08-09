from re import sub

def to_camel_case(text):
    return sub(r"(-|_)([a-zA-Z])", lambda match: match.group(2).upper(),text)