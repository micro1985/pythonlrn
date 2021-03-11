print("Enter numbers")

mx = 0

'''
while True:
    a = int(input("Enter number: "))
    if a == 13:
        break
    elif a > mx:
        mx = a
'''
a = 0
while a != 13:
    a = int(input("Enter number: "))
    if a > mx:
        mx = a

print("Maximum:", mx)
