
d3 = {'Ivanov': 21, 'Sidorov': 23,'Petrov': 25}
print(d3)

d3['Sidorovv'] = 28
print(d3)

d3.pop('Sidorovv')
print(d3)

del d3['Petrov']
print(d3)

d3.clear()
print(d3)

'''
d3['Sidorov'] = 54
print(d3)

d = {}
print(type(d))

d1 = dict()
print(type(d1))


d2 = {'Ivanov': 21}
print(d2)

print(d3['Petrov'])

print(d3.get('Vasya'))

if d3.get('Vasya') is None:
    print("ЭЭЭЭ Вуасьяя")

print(d3.get('Vasya', "Nety"))

print(d3.keys())
print(d3.values())

for i in d3:
    print(i)

for k, v in d3.items():
    print(k, v)
'''
