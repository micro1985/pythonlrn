from math import sqrt

a = int(input("Input first number: "))
b = int(input("Input second number: "))
c = int(input("Input third number: "))

D = b**2 - 4*a*c

if D >= 0:
    x1 = (-b + sqrt(D))/(2*a)
    print(x1)
    x2 = (-b - sqrt(D))/(2*a)
    print(x2)
else:
    print("No solution")

print(D)
