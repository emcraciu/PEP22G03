# INT
number1 = 3
print(type(number1))
print('Address for int is:', id(number1))

number2 = int('3')
print('Nr as text', type(number2))
print('Address for int is:', id(number2))

print('Check numbers', number1 == number2)
print('Check numbers', number1 is number2)

# float
number = 3.1
print(type(number))
print('Address for float is:', id(number))

number = float('3')
print('Nr as text', type(number))

# bool
# True_ = 3
bool_object = False
print(type(bool_object))
print('Address for bool is:', id(bool_object))

print('Convert to bool: ', bool(1))
print('Convert to int: ', int(True))

print('Convert to bool: ', bool(0))
print('Convert to int: ', int(False))

print('True and False is: ', True and False)
print('True or False is: ', True or False)
print('1 or False is: ', 1 or False)
print('True or 1 is: ', True or 1)

print('a or 1 is: ', 'a' or (1))

print(bool(0), bool(0.0), bool(0+0j), bool(False), bool(''))

print(bool(' '), bool(True), bool(-100), bool(0.1), bool(0+2j))

print('True xor 1 is: ', True.__xor__(False))

print(not (True and False))

# print('a'.__add__('b'))

# Input

# my_value = input()
# print('you entered: ', my_value)

# complex numbers

# my_number = 1 + 4j
# print(type(my_number))
#
# my_number = 0 + 3j
# print(type(my_number))
# print(my_number)
#
# print(2 / 3)  # 0.(6)
#
# my_number = (-4) ** (1 / 2)
# print(my_number)
