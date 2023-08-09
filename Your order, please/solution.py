from re import findall

def order(sentence):
    
    if not sentence:
        return sentence
    
    word_order = {}
    for word in sentence.split(' '):
      num = findall(r"\d+", word)
      word_order[int(num[0])] = word
      
    return " ".join(word for key, word in (sorted(word_order.items())))