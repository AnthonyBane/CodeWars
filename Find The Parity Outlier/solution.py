def find_outlier(integers):
    odd_list = []
    even_list = []
    for num in integers:
        if num % 2 == 0 and len(even_list) < 2:
            even_list.append(num)
        elif num % 2 != 0 and len(odd_list) < 2:
            odd_list.append(num)
        if len(even_list) == 2 and len(odd_list) == 1:
            return odd_list[0]
        elif len(odd_list) == 2 and len(even_list) == 1:
            return even_list[0]