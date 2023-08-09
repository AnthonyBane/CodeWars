def delete_nth(order,max_e):
    seen = {}
    
    return_list = []
    
    for num in order:
        if num not in seen:
            seen[num] = 1
        else:
            seen[num] += 1
        
        if seen[num] <= max_e:
            return_list.append(num)
            
    return return_list