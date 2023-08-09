def move_zeros(lst):
    num_list = []
    zero_list = []
    for index, num in enumerate(lst, start = 0):
        if num:
            num_list.append(num)
        else:
            zero_list.append(num)
    
    return num_list + zero_list