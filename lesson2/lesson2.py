iters = int(input("Enter quantity of iterations: "))

print("Input", iters, "numbers")

mx = 0

for i in range(iters):
    a = int(input("Input number: "))
    if a > mx:
        mx = a

print("Maximum:", mx)

