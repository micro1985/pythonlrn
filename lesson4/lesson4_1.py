with open("data1.txt", mode='r') as f1:
    numSet1 = {int(line.strip()) for line in f1}

print(numSet1)
