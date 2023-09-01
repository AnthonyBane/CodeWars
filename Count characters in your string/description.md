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

Just read a nice way to simplify this if statement [here](https://levelup.gitconnected.com/stop-using-dict-key-to-access-values-in-python-dictionaries-7ab45bb7946c). Rewritten to account for it:

``` python
def count_v2(s):
    character_count_dict = {}
    for char in s:
        character_count_dict[char] = character_count_dict.get(char, 0) + 1

    return character_count_dict
```