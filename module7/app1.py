class Product:

    def __init__(self):
        self.category = input("Introduceti numele categoriei: ")
        self.name = input("Introduceti numele produsului: ")
        self.price = input("Introduceti pretul produsului: ")
        self.stock = input("Introduceti stocul produsului: ")
        Categori(self)

    def __repr__(self):
        return 10 * "=" + "\n" + f"Categoria: {self.category}" + "\n" + 10 * "=" + "\n" + f"Numele: {self.name}" + "\n" + f"Pretul: {self.price}" + "\n" + f"Stocul: {self.stock}" + "\n" + 20 * "-"


class Categori:
    camasi = []
    accesorii = []
    incaltaminte = []

    def __init__(self, produs: Product):
        if produs.category == 'Camasi':
            self.camasi.append(produs)

        elif produs.category == 'Acesorii':
            self.accesorii.append(produs)

        elif produs.category == 'Incaltaminte':
            self.incaltaminte.append(produs)


lista_produse = []

# while True:
#     meniu = input("""Optiuni
#     1.Categori
#     2.Produse
#     3.Iesire""")
#     if meniu == '1':
#         submeniu1 = input(
#             """CATEGORII
#             1.Camasi
#             2.Acesorii
#             3.Incaltaminte""")
#         if submeniu1 == '1':
#             for product in lista_produse:
#                 if product.category == 'Camasi':
#                     print(product)
#         elif submeniu1 == '2':
#             for product in lista_produse:
#                 if product.category == 'Acesorii':
#                     print(product)
#         elif submeniu1 == '3':
#             for product in lista_produse:
#                 if product.category == 'Incaltaminte':
#                     print(product)
#
#
#     elif meniu == '2':
#         submeniu2 = input(
#             """Produse
#             1.Adaugare produs
#             2.Vizualizare produs
#             3.Iesire meniu principal""")
#         if submeniu2 == "3":
#             continue
#         elif submeniu2 == '1':
#             produs1 = Product()
#             lista_produse.append(produs1)
#             continue
#         elif submeniu2 == '2':
#             for produs in lista_produse:
#                 print(produs)
#             continue
#     elif meniu == '3':
#         break


while True:
    meniu = input("""Optiuni
    1.Categori
    2.Produse
    3.Iesire""")
    if meniu == '1':
        submeniu1 = input(
            """CATEGORII
            1.Camasi
            2.Acesorii
            3.Incaltaminte
            4.Add category""")
        if submeniu1 == '1':
            for product in Categori.camasi:
                print(product)
        elif submeniu1 == '2':
            for product in Categori.accesorii:
                print(product)
        elif submeniu1 == '3':
            for product in Categori.incaltaminte:
                print(product)
        elif submeniu1 == '4':
            # setattr(Categori(lista_produse[0]), input('Category name'), [] )
            Categori(lista_produse[0]).__setattr__(input('Category name'), [])


    elif meniu == '2':
        submeniu2 = input(
            """Produse 
            1.Adaugare produs
            2.Vizualizare produs
            3.Iesire meniu principal""")
        if submeniu2 == "3":
            continue
        elif submeniu2 == '1':
            produs1 = Product()
            lista_produse.append(produs1)
            continue
        elif submeniu2 == '2':
            for produs in lista_produse:
                print(produs)
            continue
    elif meniu == '3':
        break
