def longest_consec(strarr, k):
    if k > len(strarr) or len(strarr) == 0 or k <= 0:
        return ""

    if k == len(strarr):
        return "".join(strarr)
    
    largest = ""
    
    for index in range(len(strarr) - k + 1):
        new_string = "".join(strarr[index:index+k])
        if len(new_string) > len(largest):
            largest = new_string
    
    return largest
    
    
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail", "zas", "abigail", "theta"], 2))
print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2))
