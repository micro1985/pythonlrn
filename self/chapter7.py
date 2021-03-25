print("reading the file\n")
file = open("read_it.txt", "r", encoding='utf-8')
print(file.read(18))
file.close()
