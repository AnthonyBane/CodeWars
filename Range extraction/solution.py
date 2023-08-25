def solution(args):
    list_of_nums = []

    last_num = args[0]
    current_list = [last_num]

    for num in args[1:]:
        if num == last_num + 1:
            last_num = num
            current_list.append(num)
            if num == args[-1] and len(current_list) > 2:
                list_of_nums.append(
                    "-".join((str(current_list[0]), str(current_list[-1])))
                )
            elif num == args[-1] and len(current_list) == 2:
                list_of_nums.append(str(current_list[0]))
                list_of_nums.append(str(current_list[1]))
            continue

        if len(current_list) == 1:
            list_of_nums.append(str(current_list[0]))
        elif len(current_list) == 2:
            list_of_nums.append(str(current_list[0]))
            list_of_nums.append(str(current_list[1]))
        elif len(current_list) > 2:
            list_of_nums.append("-".join((str(current_list[0]), str(current_list[-1]))))

        if num == args[-1]:
            list_of_nums.append(str(num))
        last_num = num
        current_list = [last_num]

    return ",".join(num for num in list_of_nums)
