def findMax(stopValue=13):
    mx = 0
    while True:
        a = int(input("Enter number: "))
        if a == stopValue:
            break
        elif a > mx:
            mx = a
    print("Maximum:", mx)

def printHelloMyPadovan():
    print("Hello Padovan of mine")

#stpVl = int(input("Enter stop value: "))

printHelloMyPadovan()
#findMax(stpVl)
findMax()

print(findMax())

