# CodeWars Python Solutions

---

## Write Number in Expanded Form


[Link to CodeWars](https://www.codewars.com/kata/5842df8ccbd22792a4000245) 

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out part 2!!

### Solution

``` Python
def expanded_form(num):
    return_string = ""
    for index, char in enumerate(str(num), start = 1):
        if char != "0":
            if len(return_string) > 0:
                return_string += " + "
            return_string += (char) + ("0"*(len(str(num)) - index))
            
    return return_string
```

### Solution 2

Modified statement to be a 1-liner. I dislike this as it reduces readability but it was good practice.

``` Python
def expanded_form(num):
    return " + ".join(char + ("0" * (len(str(num)) - index)) for index, char in enumerate(str(num), start = 1) if char != "0") 
```