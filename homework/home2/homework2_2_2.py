#Вариант, если сравниваемое значение более одного символа

def get_less(seq=0,number=0):
    seq = str(seq)
    number = str(number)
    sm = " "
    for i in range(0, len(seq), len(number)):
        c = i + len(number)
        if int(seq[i:c]) < int(number):
            sm += seq[i:c]

    return int(sm)


a = int(input("Enter sequence: "))
b = int(input("Enter number for compare: "))
newseq = get_less(a,b)

print("The new sequence is:",newseq)
