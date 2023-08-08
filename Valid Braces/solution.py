def valid_braces(string):
    
    brace_left = ['(', '[', '{']
    brace_right = [')',']', '}']
    
    stack = []
    for brace in string:
        if brace in brace_left:
            stack.append(brace)
        elif brace in brace_right:
            brace_position = brace_right.index(brace)
            if len(stack) > 0 and (brace_left[brace_position] == stack[len(stack) -1]):
                stack.pop()
            else:
                return False
        else:
            return False
                
    return len(stack) == 0