def max_sequence(arr):
    if len(arr) == 0 or len([ele for ele in arr if ele > 0]) == 0:
        return 0
    
    pointer = 0
    count = max_count = 0
    
    while pointer <= len(arr) - 1:
        if count + arr[pointer] <= 0:
            pointer += 1
            count = 0
        else:
            count += arr[pointer]
            if count > max_count:
                max_count = count
            pointer += 1
        pass
            
    return max_count