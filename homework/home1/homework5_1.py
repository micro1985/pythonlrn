string = str(input("Input string: "))

quant = 0

VOWELS = "aoeiuy"

for letter in string:
    if letter.lower() in VOWELS:
        quant += 1
    
print("Letters quantity:",quant)

