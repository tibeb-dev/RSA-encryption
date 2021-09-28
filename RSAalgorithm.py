import random

# Returns the gcd of two numbers(num_1 and num_2) recursively by using euclid's algorithm.
def gcd(num_1, num_2):
    if num_2 == 0:
        return num_1
    else:
        return gcd(num_2, num_1 % num_2)
    
# Since a = b mod(c) iff c|(a-b) and from multiplicative inverse theorem ab = 1 mod(c), where 'b' is multiplicative inverse of 'a'. Therefore, c|(ab-1) must be true.
def multiplicative_inverse(e, totient):
    for i in range(totient):
        if ((e * i) - 1) % totient == 0:
            return i
    
def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher

