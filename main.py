import sys
from primecheck import miller_rabin_test
from primegen import generate_prime
from keygen import generate_key
from encrypt import encrypt
from decrypt import decrypt

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <command> <arguments>")
        print("\nCommands:")
        print("  primecheck <number>: Check if a number is prime")
        print("  primegen <bits>: Generate a prime number with the specified number of bits")
        print("  keygen <prime1> <prime2>: Generate RSA key pair")
        print("  encrypt <n> <e> <plaintext>: Encrypt plaintext using RSA public key")
        print("  decrypt <n> <d> <ciphertext>: Decrypt ciphertext using RSA private key")
        sys.exit(1)

    command = sys.argv[1]

    if command == "primecheck":
        argument = int(sys.argv[2])
        is_prime = miller_rabin_test(argument)
        print(is_prime)
    elif command == "primegen":
        argument = int(sys.argv[2])
        prime_number = generate_prime(argument)
        print(prime_number)
    elif command == "keygen":
        if len(sys.argv) != 4:
            print("Usage: python main.py keygen <prime1> <prime2>")
            sys.exit(1)
        p = int(sys.argv[2])
        q = int(sys.argv[3])
        if not (miller_rabin_test(p) and miller_rabin_test(q)):
            print("Both numbers must be prime.")
            sys.exit(1)
        public_key, private_key = generate_key(p, q)
        print("Public key (n, e):", public_key)
        print("Private key (n, d):", private_key)
    elif command == "encrypt":
        if len(sys.argv) != 5:
            print("Usage: python main.py encrypt <n> <e> <plaintext>")
            sys.exit(1)
        n = int(sys.argv[2])
        e = int(sys.argv[3])
        plaintext = int(sys.argv[4])
        ciphertext = encrypt((n, e), plaintext)
        print(ciphertext)
    elif command == "decrypt":
        if len(sys.argv) != 5:
            print("Usage: python main.py decrypt <n> <d> <ciphertext>")
            sys.exit(1)
        n = int(sys.argv[2])
        d = int(sys.argv[3])
        ciphertext = int(sys.argv[4])
        plaintext = decrypt((n, d), ciphertext)
        print(plaintext)
    else:
        print("Invalid command. Please use 'primecheck', 'primegen', 'keygen', 'encrypt', or 'decrypt'.")

if __name__ == "__main__":
    main()
