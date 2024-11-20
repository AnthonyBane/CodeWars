def series_sum(n):
    if n == 1:
        return "1.00"

    result = 0
    denominator = 1
    for _ in range(1, n + 1):
        result += 1 / denominator
        denominator += 3
    return f"{result:.2f}"
