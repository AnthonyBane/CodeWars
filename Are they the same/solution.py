def comp(array1, array2):
    # Just because you can doesn't mean you should! Horrible 1-linter to read
    return all(a**2 == b for a,b in zip(sorted([abs(ele) for ele in array1]), sorted(array2))) if (array1 and array2) or (array1 == [] and array2 == []) else False