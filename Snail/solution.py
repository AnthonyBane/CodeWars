def snail(snail_map):
    """
        Plan - slice the array to get right, down, left, up, append to one, another, pass the new array back in as required 
    """
    
    if len(snail_map) == 1:
        return snail_map[0]    
    
    if not len(snail_map):
        return []
    
    # Added vars for clarity sake
    right = [element for element in snail_map.pop(0)]
    down = [row.pop() for row in snail_map]
    left = [element for element in snail_map.pop()[::-1]]
    up = [row.pop(0) for row in snail_map[::-1]]
    
    return [*right, *down, *left, *up, *snail(snail_map)]