def decrypt(private_key, ciphertext):
    n, d = private_key
    plaintext = pow(ciphertext, d, n)
    return plaintext
