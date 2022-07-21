# using mutable objects as class variables

class My_Class:
    my_list = []
    my_string = ""


my_class1 = My_Class()
print(id(My_Class.my_list))
print('Initial value', my_class1.my_list)
print('My list inst 1 ID1', id(my_class1.my_list))
my_class1.my_list.append(1)
print('My list inst 1 ID2', id(my_class1.my_list))
print('Value after change', my_class1.my_list)

print('Initial str value', my_class1.my_string)
print('My str inst 1 ID1', id(my_class1.my_string))
my_class1.my_string += '1'
print('My str inst 1 ID2', id(my_class1.my_string))
print('Value str after change', my_class1.my_string)

print(80 * '#')
my_class2 = My_Class()
print('Initial value', my_class2.my_list)
my_class2.my_list.append(2)
print('Value after change', my_class2.my_list)

print('Initial str value', my_class2.my_string)
my_class2.my_string += '2'
print('Value str after change', my_class2.my_string)

print(80 * '#')

class My_Class1:

    def __init__(self):
        self.my_new_list = []

my_class1 = My_Class1()
#print(id(My_Class1.my_new_list))
print('Initial value', my_class1.my_new_list)
print('My list inst 1 ID1', id(my_class1.my_new_list))
my_class1.my_new_list.append(1)
print('My list inst 1 ID2', id(my_class1.my_new_list))
print('Value after change', my_class1.my_new_list)

my_class2 = My_Class1()
#print(id(My_Class1.my_new_list))
print('Initial value', my_class2.my_new_list)
print('My list inst 1 ID1', id(my_class2.my_new_list))
my_class2.my_new_list.append(1)
print('My list inst 1 ID2', id(my_class2.my_new_list))
print('Value after change', my_class2.my_new_list)


