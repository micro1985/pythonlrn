import random

print("Подкидываем монетку\n")

tries = 0
quant_orel = 0
quant_reshka = 0

while tries < 100:
    storona = random.randint(1,2)
    if storona == 1:
        quant_orel += 1
    else:
        quant_reshka += 1

    tries += 1

print("Орёл выпал", quant_orel, "раз")
print("Решка выпало", quant_reshka, "раз")

input("Нажми Ввод")
