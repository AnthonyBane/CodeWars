def high(x):
    
    words = x.split()
    maximum = 0
    maximum_word = ""
    
    for word in words:
        word_count = sum(ord(c) - 96 for c in word)
        if word_count > maximum:
            maximum_word = word
            maximum = word_count
    
    return maximum_word