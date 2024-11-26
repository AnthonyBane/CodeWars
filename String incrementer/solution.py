def increment_string(strng):
    backwards_strng = strng[::-1]
    backwards_num_array = []
    num_array = []
    for char in backwards_strng:
        if char.isnumeric():
            backwards_num_array.append(char)
        else:
            break

    for i in range(len(backwards_num_array)):
        num_array.append(backwards_num_array.pop())

    if not num_array:
        return strng + "1"
    num = int("".join(num_array))
    num += 1
    if len(str(num)) > len(num_array):
        new_str = strng[: -(len(num_array))] + str(num)

    elif len(str(num)) == len(num_array):
        new_str = strng[: -(len(str(num)))] + str(num)

    else:
        new_str = strng[: -(len(str(num)))] + str(num)

    return new_str


if __name__ == "__main__":
    print(increment_string("fo99obar99"))
    # print(increment_string("foo9"))
    # print(increment_string("foobar24"))
