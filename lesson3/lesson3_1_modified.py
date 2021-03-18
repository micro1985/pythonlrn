from random import randint

def generateList(quant, minVal=0, maxVal=100):

    lst = [x for x in range(quant)]
    
    lst = []
    for i in range(quant):
        lst.append(randint(minVal,maxVal))

    print(lst)
    return lst

def funcMinMaxAliquot(lis,n=1):

    assert type(lis) == list
    
    mn = min(lis)
    mx = max(lis)

    print("Min: ", mn)
    print("Max: ", mx)

    aliquuotlst = []
    for i in lis:
        if i % n == 0:
            aliquuotlst.append(i)

    if aliquuotlst:
        return aliquuotlst
    else:
        print("No aliquot values!")

val = generateList(20)
alinum = int(input("Enter number for aliquot: "))
val2 = funcMinMaxAliquot(val, alinum)

print("Aliquot numbers: ", val2)
