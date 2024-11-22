# CodeWars Python Solutions

---

## The highest profit wins

[Link to CodeWars](https://www.codewars.com/kata/559590633066759614000063)

### Description

#### Story

Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.

#### Task

Write a function that returns both the minimum and maximum number of the given list/array.

#### Examples (Input --> Output)

```
[1,2,3,4,5] --> [1,5]
[2334454,5] --> [5,2334454]
[1]         --> [1,1]
```

#### Remarks

All arrays or lists will always have at least one element, so you don't need to check the length. Also, your function will always get an array or a list, you don't have to check for null, undefined or similar.

### Solution

```py
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
```
