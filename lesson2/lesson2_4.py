def getSum(x=0, y=0, op='+'):
    if op == '+':
        return x + y
    elif op == '*':
        return x * y
    elif op == '-':
        return x - y
    else:
        return None

#z = getSum(6 ,4)
#print("Z =", z)
#print("ne Z =", getSum(12, 15))

print("Sum:",getSum(5, 3))
print("Multiply:",getSum(3, 5, '*'))
print("Difference:",getSum(7, 3, '-'))
