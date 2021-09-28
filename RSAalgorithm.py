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
def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher

