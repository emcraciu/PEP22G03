# tuples

my_tuple = ("a", 1, None, 'a')
print(type(my_tuple))

# tuple methods

result = my_tuple.count('a')
print(f'Numarul de obiecte in tuple: {result}')

print(len(my_tuple))

# tuple slice

result = my_tuple[1:3]
print('slice:',result)

# unpacking tuple
var1, var2, var3, var4 = my_tuple

print(var1, var2, var3, var4)

# packing tuple
var1, *var2, var3 = my_tuple

print(var1, var2, var3)

*var1, var2, var3 = my_tuple

print(var1, var2, var3)


# args as tuple
def my_print(args, *args2):
    print(type(args))
    print(args)

    print(type(args2))
    print(args2)


my_print('value1', 'value2', '123', 'abcd')  # dynamic number of arguments

# dictionary

my_dict = {'key1': None, 123: 'abcd', True: (1, 2, 3)}

print(my_dict)
print(type(my_dict))

# dict methods
print(my_dict.keys())
for key in my_dict.keys():
    print(key)

print(my_dict.values())
for value in my_dict.values():
    print(value)

print(my_dict.items())
for item in my_dict.items():
    print(item)

for key, value in my_dict.items():
    print(key, value)

# understanding dict items

result = my_dict.items()
itered = result.__iter__()
key, value = next(itered)
print(key, value)
key, value = next(itered)
print(key, value)
key, value = next(itered)
print(key, value)