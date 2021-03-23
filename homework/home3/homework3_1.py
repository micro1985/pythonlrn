numList = []
n = 0
quant = 0
while n >= 0:
    n = int(input("Enter positive numbers: "))
    if n >= 0:
        numList.append(n)

print("Your list: ", numList)

d = set(numList)
print("Unique numbers: ", d)
print("Quantity of unique numbers: ", len(d))

for elem in numList:
    print(elem, " => ", numList.count(elem))
