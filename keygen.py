# Function to compute the greatest common divisor (GCD) of two numbers.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """
    Function to compute the modular multiplicative inverse of a number 'a' modulo 'm'.
    It uses the extended Euclidean algorithm to find the inverse.
    """
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_key(p, q):
    """
    Function to generate RSA key pair given two prime numbers 'p' and 'q'.
    It computes 'n' as the product of 'p' and 'q', and 'phi' as the Euler's totient function.
    Then, it selects a small prime 'e' such that gcd(e, phi) = 1.
    Finally, it computes 'd' as the modular multiplicative inverse of 'e' modulo 'phi'.
    """
    n = p * q
    phi = (p - 1) * (q - 1)

    # List of small prime numbers
    small_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    
    # Select a small prime 'e' such that gcd(e, phi) = 1
    for e in small_primes:
        if gcd(e, phi) == 1:
            break

    # Compute 'd', the modular multiplicative inverse of 'e' modulo 'phi'
    d = mod_inverse(e, phi)

    return (n, e), (n, d)
