import random

def prg(s, l):
    random.seed(s)
    k = b""

    for i in range(l):
        k += bytes([random.randint(0, 255)])

    return k

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
s = int(input("Input seed: "))

p = t.encode()
k = prg(s, len(p))
c = otp_enc(t, k)
d = otp_dec(c, k)

print("Plaintext: ", to_binary(p))
print("Cipher:", to_binary(c))
print("Decrypted:", d)