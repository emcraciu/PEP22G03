# # Functii
#
# def putere_doi(x):
#     print(x * x)
#     # return None  # implicit
#
# def putere_n(x, n):
#     return x ** n
#
# print(putere_doi(3))
#
# putere_doi(3)
#
# result = putere_n(4, 5)
# print(result)
#
# print(putere_n(3, 3))


# # Argumente
#
# def putere_n(n, x, add=100, sub=0):
#     print('Valoare1 argument cheie', add)
#     print('Valoare2 argument cheie', sub)
#     print('Variabilele sunt: ', x, n)
#     return x ** n + add + sub
#
# putere_n(3, 4, add=201)
# putere_n(3, 4, 200)
# putere_n(3, 4, 200, 150)
# # putere_n(3, 4, add=200, 150)
# # print('Variabilele sunt: ', x, n) - local scope only

# Variabile

# add = 200
# sub = 100
# div = 3
# def putere_n(n, x, add=100, sub=0):
#     print('Valoare1 argument cheie', add)
#     print('Valoare2 argument cheie', sub)
#     print('Variabilele sunt: ', x, n)
#     return (x ** n + add + sub) / div
#
# print(putere_n(3,3, 25, -25))

# these vars are global
# add = 200
# sub = 100
# div = 3

# def putere_n(n, x, add=100, sub=0):
#     global div
#     print('Valoare1 argument cheie', add)
#     print('Valoare2 argument cheie', sub)
#     print('Variabilele sunt: ', x, n)
#     div = 5
#     return (x ** n + add + sub) / div
#
#
# print(putere_n(3, 3, 25, -25))
# print('Div result: ', div)


# Nested functions
arg1 = 2
def level1(arg1):
    print('inainte de modificare', arg1)
    def level2(arg2):
        nonlocal arg1
        arg1 = 10
        print(arg2 + arg1)
    level2(3)
    print('dupa modificare', arg1)

level1(1)
print('variabila globala', arg1)

