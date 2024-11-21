# CodeWars Python Solutions

---

## Sum of the first nth term of Series

[Link to CodeWars](https://www.codewars.com/kata/555eded1ad94b00403000071)

### Description

Task
Your task is to write a function which returns the n-th term of the following series, which is the sum of the first n terms of the sequence (n is the input parameter).

You will need to figure out the rule of the series to complete this.

Rules
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return "0.00".

You will only be given Natural Numbers as arguments.

```
Examples (Input --> Output)
n
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
```

### Solution

```python
def series_sum(n):
    if n == 1:
        return "1.00"

    result = 0
    denominator = 1
    for _ in range(1, n + 1):
        result += 1 / denominator
        denominator += 3
    return f"{result:.2f}"
```
