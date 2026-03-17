upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

def caesar_enc(t, shift):
    r = ""

    for char in t:
        if char in upper:
            index = upper.index(char)
            new_index = (index + shift) % 26
            r += upper[new_index]

        elif char in lower:
            index = lower.index(char)
            new_index = (index + shift) % 26
            r += lower[new_index]

        else:
            r += char

    return r


def caesar_dec(t, shift):
    return caesar_enc(t, -shift)


def affine_enc(t, a, b):
    r = ""

    for char in t:
        if char in upper:
            x = upper.index(char)
            new_index = (a * x + b) % 26
            r += upper[new_index]

        elif char in lower:
            x = lower.index(char)
            new_index = (a * x + b) % 26
            r += lower[new_index]

        else:
            r += char

    return r


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def affine_dec(t, a, b):
    r = ""
    a_inv = mod_inverse(a, 26)

    if a_inv is None:
        return "There is no modular inverse for a."

    for char in t:
        if char in upper:
            y = upper.index(char)
            new_index = (a_inv * (y - b)) % 26
            r += upper[new_index]

        elif char in lower:
            y = lower.index(char)
            new_index = (a_inv * (y - b)) % 26
            r += lower[new_index]

        else:
            r += char

    return r


t = input("Input text: ")

print("\n--- Caesar Cipher ---")
shift = int(input("Input shift: "))
enc = caesar_enc(t, shift)
print("Encrypted:", enc)
print("Decrypted:", caesar_dec(enc, shift))

print("\n--- Affine Cipher ---")
a = int(input("Input a: "))
b = int(input("Input b: "))

enc2 = affine_enc(t, a, b)
print("Encrypted:", enc2)
print("Decrypted:", affine_dec(enc2, a, b))