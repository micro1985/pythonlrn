string = input("Enter string:")

lst = []
for i in range(len(string)):
    lst.append(string[i])

string = ""
for letter in lst:
    if letter == '1':
        string += 'one'
    else:
        string += letter

print(string)
