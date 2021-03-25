from task1.writer import file_write
from task1.reader import process_data
#from task1 import writer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_write(20,"data1.txt")
    file_write(30,"data2.txt")

    process_data("data1.txt","data2.txt")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
















