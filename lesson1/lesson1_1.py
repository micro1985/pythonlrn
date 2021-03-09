# working while
'''x = 1
while x <= 10:
    if x % 2 == 0:
        print(x)
    x += 1
''' 
from random import randint

x = randint(1,10)
print(x)

c = 0
print("You have 3 attempts")
while c < 3:
    a = int(input("Hey, skinny, make your choice: "))

    b = 1

    while b < 11:
        if a == x:
            print("You`re write")
            break
        else:
            print("Wrong")
            break
    c += 1

'''for i in range(1, 11):
    if a == x:
        print("You`re write")
        #exit(0)
    else:
        print("Wrong")
        #exit(0)
'''

print("Finish")

