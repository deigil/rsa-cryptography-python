import random
from primecheck import miller_rabin_test

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if num % 2 == 0:
            num += 1
        if miller_rabin_test(num):
            return num
