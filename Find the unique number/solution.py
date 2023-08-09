def find_uniq(arr):
    seen = {}
    unique = {}
    for num in arr:
        if num not in seen:
            unique[num] = 1
            seen[num] = 1
        else:
            seen[num] = 1
            unique.pop(num, None)
            
    return next(iter(unique.keys()))