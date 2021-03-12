def check_polindrome(string=""):

#Converting string to list
    ls = []
    for i in range(len(string)):
        ls.append(string[i])

#Cheking for polindrome
    for j in range(len(ls)//2):
        if ls[j] != ls[-1-j]:
            return "It`s not polindrome"

    return "It`s polindrome"

a = input("Enter sequence: ")
res = check_polindrome(a)

print(res)
