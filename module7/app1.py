class Product:

    def __init__(self):
        self.cathegory = input("Introduceti numele categoriei")
        self.name = input("Introduceti numele produsului")
        self.cathegory = input("Introduceti pretul produsului")
        self.stock = input("Introduceti stocul produsului")

    def __repr__(self):
        return 10 * "=" + "\n" + f"Categoria: {self.cathegory}" + "\n" + 10 * "=" + "\n"


if __name__ == "__main__":
    camasi = Product()
    print(camasi)