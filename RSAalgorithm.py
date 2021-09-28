import random

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

