def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q

    # Phi is the totient of n
    totient = (p - 1) * (q - 1)

    # Choose an integer e such that e and totient(n) are coprime
    e = random.randrange(1, totient)

    # Use Euclid's Algorithm to verify that e and totient(n) are comprime
    g = gcd(e, totient)
    while g != 1:
        e = random.randrange(1, totient)
        g = gcd(e, totient)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, totient)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return (e, n), (d, n)
