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


#Returns the string from the user(which is to be decrypted) in an array form
def stringToArray(message):
    message_list = message[1:len(message) - 1].split(',')
    new_message_list = []
    for i in message_list:
        if i[0] == " ":
            new_message_list.append(int(i[1:]))
        else:
            new_message_list.append(int(i))
    return new_message_list
