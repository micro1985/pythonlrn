from random import randint

list1 = [randint(10,50) for i in range(20)]
list2 = [randint(10,50) for i in range(20)]
listUniq = []

#print("List1: ",list1, "\nList2: ", list2)

for elem in list1:
    if elem not in list2 and elem not in listUniq:
        listUniq.append(elem)

listUniq.sort()
print("Unique for List1 sorted list: ",listUniq)


listTotal = []
listTotal.extend(list1)
listTotal.extend(list2)
setTotal = set(listTotal)

print("Unique numbers for both lists: ",setTotal)

if 42 in setTotal:
    print("Yes, there is 42 in the unique list")
else:
    print("No, there is no 42 in the unique list")
