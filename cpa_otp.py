import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def xor_bytes(a, b):
    r = b""
    for i in range(len(a)):
        r += bytes([a[i] ^ b[i]])
    return r


def prf_stream(key, nonce, length):
    stream = b""
    counter = 0

    while len(stream) < length:
        block = nonce + counter.to_bytes(8, "big")

        cipher = Cipher(algorithms.AES(key), modes.ECB())
        encryptor = cipher.encryptor()
        stream += encryptor.update(block) + encryptor.finalize()

        counter += 1

    return stream[:length]


def cpa_secure_enc(text, key):
    plaintext = text.encode()
    nonce = os.urandom(8)

    keystream = prf_stream(key, nonce, len(plaintext))
    ciphertext = xor_bytes(plaintext, keystream)

    return nonce, ciphertext


def cpa_secure_dec(nonce, ciphertext, key):
    keystream = prf_stream(key, nonce, len(ciphertext))
    plaintext = xor_bytes(ciphertext, keystream)
    return plaintext.decode()


def to_binary(data):
    r = ""
    for byte in data:
        r += format(byte, "08b") + " "
    return r.strip()


t = input("Input text: ")

key = os.urandom(16)

nonce, c = cpa_secure_enc(t, key)
d = cpa_secure_dec(nonce, c, key)

print("Nonce:     ", to_binary(nonce))
print("Ciphertext:", to_binary(c))
print("Decrypted: ", d)