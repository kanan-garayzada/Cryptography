import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def xor_bytes(a, b):
    r = b""
    for i in range(len(a)):
        r += bytes([a[i] ^ b[i]])
    return r


def aes_prf(key, block):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    return encryptor.update(block) + encryptor.finalize()


def prg_from_prf(key, nonce, length):
    stream = b""
    counter = 0

    while len(stream) < length:
        counter_bytes = counter.to_bytes(16, "big")
        block = xor_bytes(nonce, counter_bytes)
        stream += aes_prf(key, block)
        counter += 1

    return stream[:length]


def cpa_secure_enc(key, message):
    message_bytes = message.encode("utf-8")
    nonce = os.urandom(16)

    pad = prg_from_prf(key, nonce, len(message_bytes))
    ciphertext = xor_bytes(message_bytes, pad)

    return nonce, ciphertext


def cpa_secure_dec(key, nonce, ciphertext):
    pad = prg_from_prf(key, nonce, len(ciphertext))
    plaintext_bytes = xor_bytes(ciphertext, pad)
    return plaintext_bytes.decode("utf-8")


def to_binary(data):
    r = ""
    for byte in data:
        r += format(byte, "08b") + " "
    return r.strip()


key = os.urandom(16)
message = input("Input message: ")

nonce, ciphertext = cpa_secure_enc(key, message)
decrypted = cpa_secure_dec(key, nonce, ciphertext)

print("Ciphertext: ", to_binary(ciphertext))
print("Decrypted:  ", decrypted)
