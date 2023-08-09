def dig_pow(n, p):
    # your code
    k = (sum(int(digit) ** index for index,digit in enumerate(str(n),start=p)))/n
    return k if k.is_integer() else -1