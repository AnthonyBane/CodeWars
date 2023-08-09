def find_nb(m):
    
    found = False
    n = 1
    total_previous = 0
    
    while not found:
        check = n**3 + total_previous
        
        if check > m:
            return -1
        
        if check == m:
            return n
        
        n += 1
        total_previous = check