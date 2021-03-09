string = str(input("Input string: "))

lns = len(string)
quant = 0

match = "a"
quant += len(string.split(match)) - 1
match = "A"
quant += len(string.split(match)) - 1
match = "o"
quant += len(string.split(match)) - 1
match = "O"
quant += len(string.split(match)) - 1
match = "e"
quant += len(string.split(match)) - 1
match = "E"
quant += len(string.split(match)) - 1
match = "i"
quant += len(string.split(match)) - 1
match = "I"
quant += len(string.split(match)) - 1
match = "u"
quant += len(string.split(match)) - 1
match = "U"
quant += len(string.split(match)) - 1
match = "y"
quant += len(string.split(match)) - 1
match = "Y"
quant += len(string.split(match)) - 1

print("Letters quantity: ",quant)

