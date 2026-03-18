import os

def generate_key(l):
    return os.urandom(l)

def to_binary(data):
    r = ""
    for b in data:
        r += format(b, "08b") + " "
    return r.strip()

def otp_enc(t, k):
    r = b""
    text_bytes = t.encode()

    for i in range(len(text_bytes)):
        r += bytes([text_bytes[i] ^ k[i]])

    return r

def otp_dec(c, k):
    r = b""

    for i in range(len(c)):
        r += bytes([c[i] ^ k[i]])

    return r.decode()


t = input("Input text: ")

p = t.encode()
k = generate_key(len(p))
c = otp_enc(t, k)
d = otp_dec(c, k)

print("Plaintext: ", to_binary(p))
print("Cipher:", to_binary(c))
print("Decrypted:", d)