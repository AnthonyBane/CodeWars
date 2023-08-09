from collections import Counter

def is_valid_walk(walk):

    if len(walk) != 10:
        return False
  
    coordinates_dict = Counter(walk)
    vertical = coordinates_dict["n"] - coordinates_dict["s"]
    horizontal = coordinates_dict["e"] - coordinates_dict["w"]
    
    return vertical == 0 and horizontal == 0