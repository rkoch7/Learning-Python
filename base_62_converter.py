import math
import sys
import string

chars = (string.digits + string.ascii_letters)
char_map = {key : idx for idx, key in enumerate(chars)}
base = len(char_map)

def encode(id):
    if(id == 0):
        return char_map[0]
    s = []
    while(id > 0):
        s.append(chars[id % base])
        id //= base

    return ''.join(s[::-1])


def decode(str_key):

    integer_sum = 0
    reversed_str = str_key[::-1]
    for idx, char in enumerate(reversed_str):
        integer_sum += char_map[char] * int(math.pow(base,idx))
    return integer_sum

e = encode(255)
print(e, type(e))
print(decode(e))