import re

def solution(s):
    return " ".join(re.findall(r'[a-zA-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', s))