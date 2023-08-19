# CodeWars Python Solutions

---

## Maximum subarrry sum


[Link to CodeWars](https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c) 

### Description

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

``` python
max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
```

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

### Solution

``` python
def max_sequence(arr):
    if len(arr) == 0 or len([ele for ele in arr if ele > 0]) == 0:
        return 0
    
    pointer = 0
    count = max_count = 0
    
    while pointer <= len(arr) - 1:
        if count + arr[pointer] <= 0:
            pointer += 1
            count = 0
        else:
            count += arr[pointer]
            if count > max_count:
                max_count = count
            pointer += 1
        pass
            
    return max_count
```
