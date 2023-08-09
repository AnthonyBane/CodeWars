import re

def is_pangram(s):
    return len("".join(filter(str.isalpha, set(s.lower())))) == 26