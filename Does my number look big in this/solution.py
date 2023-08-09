def narcissistic( value ): 
    return value == sum([int(val)**(len(str(value))) for val in str(value)])