def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    q = a // b
    r = a - q * b

    gcd, x1, y1 = extended_gcd(b, r)

    x = y1
    y = x1 - q * y1

    return gcd, x, y


a = int(input("Input a: "))
b = int(input("Input b: "))

gcd, x, y = extended_gcd(a, b)

print("gcd =", gcd)
print("x =", x)
print("y =", y)
print(f"{a}*({x}) + {b}*({y}) = {gcd}")