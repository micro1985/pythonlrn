numSet = []
with open('D:/DevOps/repos/pythonlrn/homework/home3/input.txt', mode='r') as f:
    for line in f:
        numSet.append(int(line.strip()))

def getSum(listForSum):
    listSum = 0
    for i in range(len(listForSum)):
        listSum += listForSum[i]

    return listSum
                   
uniq = set(numSet)

print("MaxVal:", max(numSet))
print("MinVal:", min(numSet))
print("Sum:", getSum(numSet))
print("Uniq quant:", len(uniq))

