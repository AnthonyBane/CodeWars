# CodeWars Python Solutions

---

## Count characters in your string


[Link to CodeWars](https://www.codewars.com/kata/52efefcbcdf57161d4000091) 

### Description

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

### Solution

``` python
def count(s):
    character_count_dict = {}
    for char in s:
        if char in character_count_dict:
            character_count_dict[char] += 1
        else:
            character_count_dict[char] = 1

    return character_count_dict
```