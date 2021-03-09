a = int(input("Input first number: "))
b = int(input("Input second number: "))
c = int(input("Input third number: "))

if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
elif c < a and c < b:
    print(c)
