string = input("Enter string:")
string2 = string
string = ""
for i in range(len(string2)):
    if string2[i] == '1':
        string += 'one'
    else:
        string += string2[i]

print(string)
