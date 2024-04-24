# 🛡️ RSA Cryptography with Python 🐍

Welcome to RSA Cryptography implementation in Python! This guide will walk you through how to use the `main.py` script to perform various cryptographic operations.

## How to Use

1. **Clone the Repository**: First, clone the repository containing the Python scripts for RSA implementation.

2. **Navigate to Directory**: Open your terminal and navigate to the directory where the Python scripts are located.

3. **Run `main.py`**: Execute the `main.py` script with Python by providing the appropriate command and arguments.

    ```bash
    python main.py <command> <arguments>
    ```

4. **Available Commands**:
   
   - **primecheck**: Check if a number is prime.
   - **primegen**: Generate a prime number with the specified number of bits.
   - **keygen**: Generate RSA key pair.
   - **encrypt**: Encrypt plaintext using RSA public key.
   - **decrypt**: Decrypt ciphertext using RSA private key.

5. **Examples**:

   - **Check Primality**:
     ```bash
     python main.py primecheck 123456789
     ```

   - **Generate Prime Number**:
     ```bash
     python main.py primegen 256
     ```

   - **Generate RSA Key Pair**:
     ```bash
     python main.py keygen 1019 1021
     ```

   - **Encrypt Plaintext**:
     ```bash
     python main.py encrypt 1137523782892346560028993 11 150
     ```

   - **Decrypt Ciphertext**:
     ```bash
     python main.py decrypt 1137523782892346560028993 682514269629973045909913 864975585937500000000000
     ```

6. **Explore and Enjoy!**: Feel free to explore and experiment with different commands and arguments to better understand RSA cryptography.

Happy Cryptography! 🔐✨
