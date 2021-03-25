def process_data(filename1,filename2):
    with open(filename1, mode='r') as f1:
        #numList1 = [int(line.strip()) for line in f1]
        #numSet1 = set(numList1)
        numSet1 = {int(line.strip()) for line in f1}
    with open(filename2, mode='r') as f2:
        #numList2= [int(line.strip()) for line in f2]
        #numSet2 = set(numList2)
        numSet2 = {int(line.strip()) for line in f2}

    #numSet3 = set(numSet1.union(numSet2))
    print("Intersection: ", numSet2.intersection(numSet1))
    print("Union: ", numSet1.union(numSet2))
    print("Count: ", len(numSet1.union(numSet2)))
