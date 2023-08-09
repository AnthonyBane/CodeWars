from textwrap import wrap

def solution(s):
    return [combo if len(combo) == 2 else (combo + "_") for combo in wrap(s, 2)]