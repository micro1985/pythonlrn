string = str(input("Input string: "))

quant = 0

vowels = "aAoOeEiIuUyY"

for letter in string:
    if letter in vowels:
        quant += 1
    
print("Letters quantity: ",quant)

