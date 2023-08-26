def order_weight(strng):
    if not strng:
        return ""
        
    calculated_weights = {}
    for word in strng.split(" "):
        weight = sum(int(char) for char in word)
        if weight in calculated_weights:
            calculated_weights[weight].append(word)
        else:
            calculated_weights[weight] = [word]

    sorted_calculated_weights = {}
    for weight, word_list in calculated_weights.items():
        sorted_calculated_weights[weight] = " ".join(sorted(word_list))
        
    sorted_weights = sorted(sorted_calculated_weights.items(), key=lambda x: x[0])
    return " ".join(weight[1] for weight in sorted_weights)
