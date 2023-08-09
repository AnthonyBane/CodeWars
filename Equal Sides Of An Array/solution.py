def find_even_index(arr):
    
    for index in range(len(arr)):
        left = sum(arr[:index])
        right = sum(arr[index + 1:])
        
        if left == right:
            return index
    
    return -1