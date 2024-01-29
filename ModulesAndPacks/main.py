import functions
from data import my_dict
from classes import MyClass

print('This is executed file')

if __name__ == "__main__":
    print('The code below wont be executed if this file will be an import module to another executed file')
    print(functions.get_double_number(100))
    print(my_dict)
    MyClass()
