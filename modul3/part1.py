# my_age = 14
#
# if my_age >= 18:
#     print('You are an adult')
# elif my_age >= 13:
#     print('you are a teenager')
# elif my_age >= 0:
#     print('you are a child')
# else:
#     print('Negative values are nto allowed')
#
# print('dONE')

# # AND WITH CONDITION
#
# a = ""
# b = False
#
# if a:
#     print(b)
# else:
#     print(a)
#
# print(a and b)
#
# # OR WITH CONDITION
#
# if a:
#     print(a)
# else:
#     print(b)
#
# print(a or b)


# # condition
# a = ""
# b = "b"
#
# print(a and b)
# print(bool(a and b))
# print(bool(a))

#
# print(2000 - True)
# print(True > 2000)
# print(dir(True))


# while loop

# depends_on = 1
#
# while depends_on <= 4:
#     depends_on += 1
#     print('Running')
#     if depends_on == 4:
#         break
#
#
# print('Done')


# n = 0
# while n < 10:
#     if n == 7:
#         n += 1
#         continue
#     print(n)
#     n += 1
#
# print('Done')


n = 0
while n < 6:
    if n == 7:
        n += 1
        break
    print(n)
    n += 1
else:
    print('Done')