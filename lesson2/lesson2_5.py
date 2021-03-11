def enterNum():
    iters = 6
    a = []
    for i in range(iters):
        a.append(int(input("Enter numbers: ")))
    
    a.sort(reverse=True)
    
    return a
    
res = enterNum()

print(res)
