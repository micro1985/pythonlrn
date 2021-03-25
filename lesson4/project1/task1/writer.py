from random import randint


def file_write(count, filename):
    with open(filename, mode='w') as fw:
        for x in range(count):
            fw.write(str(randint(10,50)) + "\n")