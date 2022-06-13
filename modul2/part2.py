# my_text = "My Python3 Course"
#         #  0123456789
#
# # Slice with single value
# print(my_text)
# print(my_text[9])
#
# # Slice with start and stop value
# print(my_text[3:9])
# print('No start value: ', my_text[:9])
# print('No stop value: ', my_text[3:])
# print('With stop value: ', my_text[3:17])
#
# # Slice with start stop and step value
# print(my_text[3:9:1])
# print(my_text[3:9:2])
# print(my_text[3:9:2])
#
# print('No start value: ', my_text[:9:2])
# print('No stop value: ', my_text[3::2])
# print('No step value: ', my_text[3:9:])

my_text = "My Python3 Course"
#           -5-4-3-2-1


# # Slice with single negative value
print(my_text)
print(my_text[-2])

# Slice with start and stop value
print(my_text[-3:-1])
# print('No start value: ', my_text[:9])
# print('No stop value: ', my_text[3:])
# print('With stop value: ', my_text[3:17])
#
# Slice with start stop and negative step value
print(my_text[-1:-5:-1])
# print(my_text[-1:-5:0])

print('No start value: ', my_text[9::-1])

# String methods and functions

# len() function
my_string = "Hello Python"
print('Length is : ', len(my_string))
print('Length is : ', my_string.__len__())

my_string = ""
print('Length is : ', len(my_string))

# Format

my_string = "Hello Python {}"

print('Formatted text: ', my_string.format('abcd'))

my_string = "Hello Python {0} {1} {2}"

print('Formatted text: ', my_string.format('a', 'b', 'c'))

my_string = "Hello Python {enva} {envb} {envc}"

print('Formatted text: ', my_string.format(enva='a', envb='b', envc='c'))


# String types

# Normal string
normal1 = "Normal string \n"
normal2 = 'Normal \n string'

# Multiline string
normal1 = """Normal string \n
New line"""
print(normal1)
normal2 = '''Normal 
             string'''
print(normal2)

# raw string
normal1 = r"""Normal string \n
New line"""

print(normal1)

# formatted string
var1 = "insert"
normal1 = f"""Normal string {var1}
New line"""

# replace method
var1 = "insert insert insert"
var1 = var1.replace('ins', '_', 2)
print('Replaced i: ', var1)


