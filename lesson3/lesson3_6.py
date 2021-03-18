'''
with open('D:/vm/Python/labs/python_3/input5.txt', mode='w') as f:
    f.write('Test test')
'''

with open('D:/vm/Python/labs/python_3/input5.txt', mode='a') as f:
    f.write('\nEngineering!!!')

with open('D:/vm/Python/labs/python_3/input5.txt', mode='r') as f:
    for line in f:
        print(line.strip())
    
