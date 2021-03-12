def check_polindrome(string=""):

#Making lower case
    string = string.lower()

#Converting string to list
    ls = []
    for i in range(len(string)):
        ls.append(string[i])

#Removing unnecessary
    znaki = [",",".","!"," ","?"]

    newls = []
    for k in range(len(ls)):
        if ls[k] not in znaki:
            newls.append(ls[k])
    
#Making new string from list
    newstring = ""
    for ele in newls:
        newstring += ele
        
#Cheking for polindrome    
    for j in range(len(newls)//2):
        if newls[j] != newls[-1-j]:
            print("New string is:",newstring)
            return "It`s not polindrome"

    print("New string is:",newstring)
    return "It`s polindrome"

a = input("Enter sequence: ")
res = check_polindrome(a)

print(res)
