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
