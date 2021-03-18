def sumReturn(number=0):
    #number = str(number)
    sm = 0
    for i in range(len(number)):
        sm += int(number[i])

    return sm

a = int(input("Enter number: "))
b = sumReturn(a)

print("The sum is:",b)

