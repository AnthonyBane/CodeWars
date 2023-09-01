def sum_dig_pow(a, b):
    eureka_nums = []

    for num in range(a, b + 1):
        total = sum(int(char) ** index for index, char in enumerate(str(num), start=1))
        if total == num:
            eureka_nums.append(num)

    return eureka_nums
