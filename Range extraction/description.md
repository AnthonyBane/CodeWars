# CodeWars Python Solutions

---

## Range Extraction


[Link to CodeWars](https://www.codewars.com/kata/51ba717bb08c1cd60f00002f) 

### Description

A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

#### Example:

``` python
solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
```

### Solution

I really disliked this solution. It feels like there should have been a more simple solution.

``` python
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
```

After reviewing some of the solutions that others have come up with, I found this which I liked the most which I have tweaked to adhere to good programming standards:

``` python
def solution(arr):
    ranges = []
    first_num = last_num = arr[0]
    for current_num in arr[1:] + [None]:
        if current_num != last_num+1:
            ranges.append(str(first_num) if first_num == last_num else "{}{}{}".format(first_num, "," if first_num+1 == last_num else "-", last_num))
            first_num = current_num
        last_num = current_num
    return ",".join(ranges)
```

This was actually what I was aiming for but I couldn't think of the best formatting technique which was provided by this solution.