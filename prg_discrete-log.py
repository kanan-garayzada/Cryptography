def prg(seed, p, g, length):
    x = seed % p
    result = []
    limit = (p - 1) // 2

    for i in range(length):
        if x > limit:
            result.append(1)
        else:
            result.append(0)

        x = pow(g, x, p)

    return result


seed = int(input("Input seed: "))
p = int(input("Input prime p: "))
g = int(input("Input generator g: "))
length = int(input("Input output length: "))

bits = prg(seed, p, g, length)

print("Generated Bits:", "".join(str(b) for b in bits))