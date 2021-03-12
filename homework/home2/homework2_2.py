#Вариант, если сравниваемое значение равно одному символу

def get_less(seq=0,number=0):
    seq = str(seq)
    sm = " "
    for i in range(len(seq)):
        if int(seq[i]) < number:
            sm += seq[i]

    return int(sm)

a = int(input("Enter sequence: "))
b = int(input("Enter number for compare: "))
newseq = get_less(a,b)

print("The new sequence is:",newseq)
