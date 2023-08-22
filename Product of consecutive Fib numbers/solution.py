def productFib(prod, fib_1=0, fib_2=1):
    if prod < fib_1 * fib_2:
        return [fib_1, fib_2, False]
    if prod == fib_1 * fib_2:
        return [fib_1, fib_2, True]

    total = fib_1 + fib_2
    fib_1 = fib_2
    fib_2 = total
    return productFib(prod, fib_1, fib_2)
