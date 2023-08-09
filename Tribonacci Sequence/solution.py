def tribonacci(signature, n):
    if n == 0:
        return []
    elif n <= 3:
        return signature[0:n]
    
    first,second,third = [*signature]
    new_num = 0
    trib_array = [first,second,third]
    
    for index in range(n-(len(signature))):
        new_num = first + second + third
        trib_array.append(new_num)
        first = second
        second = third
        third = new_num
    
    return trib_array