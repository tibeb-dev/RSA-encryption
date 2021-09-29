import random
   
#checks if the given number is a prime and returns a boolean.
def isPrime(number):
    # Checking that given number is more than 1
    if number > 1:
        # Iterating over the given number with for loop
        for j in range(2, int(number/2) + 1):
            # If the given number is divisible or not
            if (number % j) == 0:
                return False
        # Else it is a prime number
        else:
            return True
    # If the given number is 1 
    else:
        return False
    
# Since a = b mod(c) iff c|(a-b) and from multiplicative inverse theorem ab = 1 mod(c),
# where 'b' is multiplicative inverse of 'a'. Therefore, c|(ab-1) must be true.

    
def multiplicativeInverse(e, totient):
    for i in range(totient):
        if (e * i) % totient == 1:
            return i
        
# Returns the gcd of two numbers(num_1 and num_2) recursively by using euclid's algorithm.
def gcd(num_1, num_2):
    if num_2 == 0:
        return num_1
    else:
        return gcd(num_2, num_1 % num_2)
       
def generateKeys(p, q):

    # In this function we follow the procedures below to generate key pairs:
    #         1, Choose two distinct prime numbers p and q
    #         2, Compute n = pq
    #         3, Compute λ(n), where λ is Carmichael's totient function. Since n = pq, λ(n) = lcm(λ(p),λ(q)),
    #            and since p and q are prime, λ(p) = φ(p) = p − 1 and likewise λ(q) = q − 1. Hence λ(n) = lcm(p − 1, q − 1).
    #         4, Choose an integer e such that 1 < e < λ(n) and gcd(e, λ(n)) = 1; that is, e and λ(n) are relatively prime.
    #         5, Determine d as d ≡ e−1 (mod λ(n)); that is, d is the modular multiplicative inverse of e modulo λ(n).

    ''' 
    In this function we follow the procedures below to generate key pairs:
            1, Check if the given numbers p and q are prime and not similar
            2, Compute n = pq
            3, Compute λ = (p - 1) * (q - 1)
            4, Choose an integer e such that 1 < e < λ and gcd(e, λ) = 1; that is, e and λ are relatively prime.
            5, Determine d as d(e) ≡ 1 (mod λ); that is, d is the modular multiplicative inverse of e modulo λ.
    '''
    if p == q:
        raise ValueError('p and q cannot be equal')
    elif not (isPrime(p) and isPrime(q)):
        raise ValueError('Both numbers must be prime.')
    n = p * q
    λ = (p - 1) * (q - 1)
    e = random.randrange(1, λ)
    temp = gcd(e, λ)
    while temp != 1:
        temp = gcd(e, λ)
        e = random.randrange(1, λ)
    d = multiplicativeInverse(e, λ)

    # return the Public key [(e, n)] and private key [(d, n)]
    return (e, n), (d, n)


#Returns the ciphertext c as array of bytes , using the public key e, corresponding to m^e ≡ c ( mod n )
    # i.e using modular exponentiation.
def encrypt(publicKey, plaintext):
    key, n = publicKey
    ciphertext = [(ord(char) ** key) % n for char in plaintext]
    return ciphertext

# Returns plaintext by recovering plaintext from cipyeshertext by using the given private key exponent d by computing:
    # c^d ≡ ( m^e )^d ≡ m ( mod n ) 
def decrypt(privateKey, ciphertext):
    key, n = privateKey
    plaintext = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plaintext)


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


public, private = 0, 0
askToGiveKeys = input("Do you need private and public keys to be generated? [Y / N] : ").lower()
if askToGiveKeys == "y":
    p = int(input("Enter a prime number: "))
    q = int(input("Enter another prime number: "))
    public, private = generateKeys(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    print("keep Your private key in a secure place")
task = input("What can i do for you? [E / D]: ").lower()

if task == "e":
    if public == 0:
        print("Please enter your public key, first the key(e) then the totient(n) from your public key(something like: (e, n):")
        key = input("Please enter your public key: ")
        totient = input("Please enter your totient value: ")
        public = (int(key), int(totient))
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(public, message)
    print("Your encrypted message is: ")
    print(encrypted_msg)
if task == "d":
    if private == 0:
        print("Please enter your private key, first the key(d) the the totient(n) from your public key(something like: (d, n):")
        key = input("Please enter your private key: ")
        totient = input("Please enter your totient value: ")
        private = (int(key), int(totient))
    message = input("Enter a message to decrypt with your private key: ")
    print("Your message is: ")
    print(decrypt(private, stringToArray(message)))
