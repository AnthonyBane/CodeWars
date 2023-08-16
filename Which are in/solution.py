def in_array(array1, array2):
    all_a2_words = ",".join(array2)
    return sorted([word for word in list(set(array1)) if word in all_a2_words])