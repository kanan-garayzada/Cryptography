def dh_public_key(g, private_key, q):
    return pow(g, private_key, q)


def dh_shared_key(other_public_key, private_key, q):
    return pow(other_public_key, private_key, q)


q = int(input("Input q: "))
g = int(input("Input g: "))

x = int(input("Input Alice private key x: "))
y = int(input("Input Bob private key y: "))

hA = dh_public_key(g, x, q)
hB = dh_public_key(g, y, q)

kA = dh_shared_key(hB, x, q)
kB = dh_shared_key(hA, y, q)

print("Alice public key hA =", hA)
print("Bob public key hB =", hB)
print("Alice shared key =", kA)
print("Bob shared key =", kB)

if kA == kB:
    print("Shared key is the same.")
else:
    print("Shared key is different.")