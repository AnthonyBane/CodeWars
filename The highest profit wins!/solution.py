def min_max(lst):
    # Could just use min() and max() but this solution only iterates
    # through the list once making it more efficient for large values of N
    min_num = lst[0]
    max_num = lst[0]
    if len(lst) == 1:
        return [lst[0]]

    for i in range(1, len(lst)):
        num = lst[i]
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num

    return [min_num, max_num]
