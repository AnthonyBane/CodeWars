# CodeWars Python Solutions

---

## Scramblies


[Link to CodeWars](https://www.codewars.com/kata/55c04b4cc56a697bb0000048) 

### Description

Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

### Notes:

1. Only lower case letters will be used (a-z). No punctuation or digits will be included.
2. Performance needs to be considered.

### Examples

``` python
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
```

### Solution

``` python
from collections import Counter


def scramble(s1, s2):
    s1_dict = Counter(s1)
    s2_dict = Counter(s2)

    return all(
        (s2_key in s1_dict) and (s2_count <= s1_dict[s2_key])
        for s2_key, s2_count in s2_dict.items()
    )
```

A great example of a more thoughtful solution is:

``` python
from collections import Counter


def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2) - Counter(s1)) == 0
```

Though this does have a negative impact of iterating through all the items before analsying the outcome. 
