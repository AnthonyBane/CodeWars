import re

def count_smileys(arr):

    return sum(1 if re.match("^[:;]{1}[-~]?[)D]{1}?$", smiley) else 0 for smiley in arr)