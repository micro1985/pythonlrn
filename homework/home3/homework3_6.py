numList1 = []
numList2 = []
listUniq1 = []
listUniq2 = []

with open('D:/DevOps/repos/pythonlrn/homework/home3/input.txt', mode='r') as f1:
    numList1 = [int(line.strip()) for line in f1]
    #for line in f1:
     #   numSet1.append(int(line.strip()))

with open('D:/DevOps/repos/pythonlrn/homework/home3/input_1.txt', mode='r') as f2:
    string = f2.read()
    string = string.strip()
    numList2 = string.split(" ")
    numList2 = [int(i) for i in numList2]
    
def checkUnique(set1, set2):
    listUniq = []
    for elem in set1:
        if elem not in set2:
            listUniq.append(elem)
    return listUniq


a = set(numList1)
b = set(numList2)

listUniq1 = checkUnique(a, b)
listUniq2 = checkUnique(b, a)

listTotal = []
listTotal.extend(numList1)
listTotal.extend(numList2)
setTotal = set(listTotal)

with open('D:/DevOps/repos/pythonlrn/homework/home3/results_1.txt', mode='w') as fw:
    fw.write("Only in file1: ")
    for x in listUniq1:
        fw.write(str(x) + " ")
    fw.write("\nOnly in file2: ")
    for y in listUniq2:
        fw.write(str(y) + " ")
    fw.write("\nAt least in one file: ")
    for z in setTotal:
        fw.write(str(z) + " ")
'''
print("List1:", len(numList1))
print("List2:", len(numList2))
print("ListTotal:", len(listTotal))
print("ListUniqueTotal:", len(setTotal))

print("Uniq for List1:", listUniq1)
print("Uniq for List2:", listUniq2)
'''
