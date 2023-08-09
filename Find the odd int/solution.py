def find_it(seq):
    dict = {}
    for num in seq:
       if num in dict:
           dict[num] = dict[num] + 1
       else:
           dict[num] = 1
           
    for num in seq:
        if dict[num] % 2 != 0:
            return num
    return None