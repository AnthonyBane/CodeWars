def remove_smallest(numbers):
    if len(numbers) < 2:
        return []

    min_value = numbers[0]
    min_index = 0
    for index in range(1, len(numbers)):
        if numbers[index] < min_value:
            min_value = numbers[index]
            min_index = index

    return [num for index, num in enumerate(numbers) if index != min_index]


if __name__ == "__main__":
    print(remove_smallest([1, 2, 3]))
