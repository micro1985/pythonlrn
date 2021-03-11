def enterNum():
    iters = 6
    a = []
    for i in range(iters):
        a.append(int(input("Enter numbers:")))
    
    a.sort()
    a.reverse()

    return a
    
b = enterNum()

print(b)
