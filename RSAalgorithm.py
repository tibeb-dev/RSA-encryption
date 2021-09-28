import random

def convert_to_ascii(ciphertext):
    cipherArray = []
    i = 0
    while i < len(str(ciphertext)):
        if i == len(str(ciphertext)) - 1:
            cipherArray.append(int(str(ciphertext)[i]))
            return cipherArray
        cipherArray.append(int(str(ciphertext)[i]) * 10 + int(str(ciphertext)[i+1]))
        i += 2
    return cipherArray

def multiplicative_inverse(e,r):
    for i in range(r):
        if (e*i)%r == 1:
            return i

