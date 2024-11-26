# CodeWars Python Solutions

---

## String incrementer

[Link to CodeWars](https://www.codewars.com/kata/54a91a4883a7de5d7800009c)

### Description

Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.

### Solution

```python
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
```

Notes:

I couldn't remember the efficient methods for stripping characters from a string so cobbled this together
using arrays and a stack. Quite inefficient through still runs in O(N).
