def gcd(a, b):
    while b != 0:
        q = a // b
        r = a - q * b
        a = b
        b = r
    return a


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    q = a // b
    r = a - q * b

    gcd_value, x1, y1 = extended_gcd(b, r)

    x = y1
    y = x1 - q * y1

    return gcd_value, x, y


def mod_inverse(e, phi):
    gcd_value, x, y = extended_gcd(e, phi)

    if gcd_value != 1:
        return None

    return x % phi


def rsa_encrypt(m, e, n):
    return pow(m, e, n)


def rsa_decrypt(c, d, n):
    return pow(c, d, n)


p = int(input("Input prime p: "))
q = int(input("Input prime q: "))
e = int(input("Input e: "))
m = int(input("Input message m: "))

n = p * q
phi = (p - 1) * (q - 1)

if gcd(e, phi) != 1:
    print("Error: gcd(e, phi(N)) must be 1")
elif m <= 0 or m >= n:
    print("Error: m must satisfy 0 < m < N")
elif gcd(m, n) != 1:
    print("Error: m must be in Z*_N, so gcd(m, N) must be 1")
else:
    d = mod_inverse(e, phi)

    c = rsa_encrypt(m, e, n)
    decrypted = rsa_decrypt(c, d, n)

    print("Ciphertext =", c)
    print("Decrypted message =", decrypted)