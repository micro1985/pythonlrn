def sumReturn(number=0):
    summa = 0
    while number > 0:
        i = number%10
        number = number // 10
        summa = summa + i
    return summa
    
a = int(input("Enter number: "))
b = sumReturn(a)

print(b)
