string = input("Enter string:")

lst = string.split(" ")

def maxCountWord(listString):
    listSet = set(listString)
    maxCount = 0
    mostPopular = None
    for word in listSet:
        count = listString.count(word)
        if count > maxCount:
            maxCount = count
            mostPopular = word

    return mostPopular

print("The lognest word:",max(lst, key=len))
print("Most popular:",maxCountWord(lst))
