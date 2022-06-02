# Problema 1
baza = input('Introduceti valoarea bazei')
inaltime = input('Introduceti valoarea inaltimii')
arie = (int(baza) * int(inaltime) / 2)
print(type(arie))
print("Aria este:", arie)


# Problema 2
parola = 7710
nr_tastatura = int(input('Introduceti nr.:'))

print('Rezultatul este:', nr_tastatura == parola)


# Problema 3
numar1 = int(input('Primul numar:'))
numar2 = int(input('Al doilea numar:'))

print(
    'Media numerelor este:', (numar1 + numar2) / 2,
    'Impartirea numerelor:', int(numar1 / numar2),
    'ridicarea la putere:', numar1 ** numar2
)


# Problema 4
venit = int(input("Venitul pe o lunae este:"))
a = 50 / 100 * venit
b = 30 / 100 * venit
c = 20 / 100 * venit

print(
    'Venituri acordate necesitatiilor:', a, '\n',
    'Venituri acordate scopuri recreationale:', b, '\n',
    'Venituri acordate datoriilor si economiilor:', c, '\n'
)


# Problema 5
a = 3
b = 4
c = 5

x = (-b + ((b ** 2 - 4 * a * c) ** (1 / 2))) / (2 * a)
print(x)
