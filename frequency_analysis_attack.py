upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_enc(t, shift):
    r = ""

    for char in t:
        if char in upper:
            index = upper.index(char)
            new_index = (index + shift) % 26
            r += upper[new_index]

        else:
            r += char

    return r


def caesar_dec(t, shift):
    return caesar_enc(t, -shift)

def frequency_checker(c):
    l = list(c)

    for char in l:
        if char in upper:
            max = char
            break

    for i in range(len(l)):
        if l[i] in upper:
            if l.count(l[i]) > l.count(max):
                max = l[i]

    return max

c = input("Input ciphertext: ").upper()
s = (upper.index((frequency_checker(c))) - upper.index("E")) % 26
print("Decrypted:", caesar_dec(c, s))
