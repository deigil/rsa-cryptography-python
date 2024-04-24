def encrypt(public_key, plaintext):
    n, e = public_key
    ciphertext = pow(plaintext, e, n)
    return ciphertext
