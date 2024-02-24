import math


def decode(s):
    num_str = ""
    for char in s:
        if char.isdigit():
            num_str += char
        else:
            break

    num = int(num_str)
    coded_s = s[len(num_str) :]
    decoded_s = ""
    for char in coded_s:
        if not char.isalpha():
            return "Impossible to decode"
        x = ord(char) - ord("a")
        if math.gcd(x, 26) != 1:
            return "Impossible to decode"  # x is not invertible modulo 26
        original_x = inverse_modulo(x, 26)
        decoded_s += chr((original_x * num) % 26 + ord("a"))
    return decoded_s


def inverse_modulo(a, m):
    return pow(a, -1, m)
