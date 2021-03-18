from random import randint

myDict = {x:x * x  for x in range(10)}
myDict2 = {x:x * x for x in range(10) if x % 2 != 0}

'''
myDict = {}
for i in range(11):
    myDict[i] = i * i
'''
print(myDict)
print(myDict2)

'''
myDict = {}

k = ['a','b','c','d','e']
for i in k:
    myDict[i] = randint(10, 100)
print(myDict)
print(len(myDict))

for k, v in myDict.items():
    if v % 2 == 0:
        print(k,v)

myDict['g'] = randint(10,100)
print(myDict)

print(max(myDict.values()))

print(min(myDict.keys()))

if 'b' in myDict:
    del myDict['b']
print(myDict)
print(sum(myDict.values()))
'''

'''
if 'm' in myDict:
    print("Yes")
else:
    print("No")
'''
