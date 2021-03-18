a = [x for x in range(10) if x % 2 == 0]
print(a)

b = []
for i in range(10):
    if i % 2 == 0:
        b.append(i)

print(b)

c = [x for x in range(1000) if x % 13 == 0]
print(c)
