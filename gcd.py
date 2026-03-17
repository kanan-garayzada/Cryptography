num1 = int(input("Input the first number: "))
num2 = int(input("Input the second number: "))

while num2 != 0:
        num1, num2 = num2, num1 % num2

print("GCD =", num1)