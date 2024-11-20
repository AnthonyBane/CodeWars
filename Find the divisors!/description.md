# CodeWars Python Solutions

---

## Find the divisors!

[Link to CodeWars](https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/python)

### Description

Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#, empty table in COBOL) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

### Solution

```python
def divisors(integer):
    if integer < 4:
        return f"{integer} is prime"

    divs = []
    for num in range(2, integer):
        if integer % num == 0:
            divs.append(num)
    if not divs:
        return f"{integer} is prime"
    return divs

```
