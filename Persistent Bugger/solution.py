from numpy import prod

def persistence(n, i=0):
    if n > 9: 
        i += 1
        i = persistence(prod([int(digit) for digit in str(n)]), i)

    return i