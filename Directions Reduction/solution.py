def dirReduc(arr):
    
    north_east = ["NORTH", "EAST"]
    south_west = ["SOUTH", "WEST"]
    
    stack = []
    
    for direction in arr:
        stack.append(direction)
        if len(stack) > 1 and (direction in north_east):
            index = north_east.index(direction)
            if stack[-2] == south_west[index]:
                stack.pop()
                stack.pop()
                
        elif len(stack) > 1 and (direction in south_west):
            index = south_west.index(direction)
            if stack[-2] == north_east[index]:
                stack.pop()
                stack.pop()
        
    return stack