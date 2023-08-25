# CodeWars Python Solutions

---

## First Non-Repeating Character


[Link to CodeWars](https://www.codewars.com/kata/52bc74d4ac05d0945d00054e) 

### Description

Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

### Solution

``` python
def first_non_repeating_letter(s):
    char_count = {}
    for index, char in enumerate(s):
        if char.lower() in char_count:
            char_count[char.lower()].append(index)
        else:
            char_count[char.lower()] = [index]
    return_char = [index for index,char in enumerate(s) if len(char_count[char.lower()]) == 1] 
    return s[return_char[0]] if return_char else ""
```