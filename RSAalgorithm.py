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

#returns the gcd of two numbers recursively by using euclid's algorithm.
def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a%b)
    
def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher

