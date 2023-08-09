def digital_root(n):
    total = sum(list(map(int,str(n))))
    if total > 9:
        total = digital_root(total)
    return total