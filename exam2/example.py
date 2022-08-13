"""
A shop needs an iterable object to keep track of product expiration dates.
Each product in the shop will have a string name, datetime expiration
Iterating the object will return all products in the shop ordered by expiration date
1) 40p: Definition
    a) 10p: Basic class structure of objects
    b) 10p: Basic class structure of iterator
    c) 10p: Method to add product to the shop
    d) 10p: Method to remove product that expired
2) 40p: Execution:
    a) 10p: Create instance of your shop
    b) 10p: Add products:
        - Banana, 11 Aug 2022
        - Orange, 12 Aug 2022
        - Kiwi, 13 Aug 2022
        - Apple, 14 Aug 2022
        - Peach, 15 Aug 2022
    c) 10p: Remove expired products
    d) 10p: Iterate the created object writing each product on a new line in file in the order of expiration
3) 20p: Documenting:
   a) 5p: type hints for arguments
   b) 5p: module documentation
   c) 5p: class documentation for all classes
   d) 5p: method documentation for all methods
"""

import datetime


class Shop:
    """Clasa magazinului"""

    produse = {}

    def __init__(self, produs: str):
        self.produs = produs
        self.day = datetime.datetime.now()

    def __iter__(self):
        return ShopIterator(self.produse)

    def add_product(self, produs, data_expirare):
        """Metoda care adauga produsul"""
        self.produse[produs] = data_expirare

    def remove_product(self):
        """Metoda care sterge produsele expirate"""
        now = datetime.datetime.now()
        for product in self.produse.copy():
            if now.day > self.produse[product].day:
                del self.produse[product]

    def write_to_file(self):
        """Metoda care scrie datele in fisier"""
        with open('my_file.out', "w") as file:
            for product in self:
                file.write(f"{str(product)}\n")


class ShopIterator():
    """Clasa iteratorului"""

    expiration_date = []

    def __init__(self, produse: dict):
        self.produse = produse
        # for key, value in self.produse.items():
        #     for produs in self.expiration_date:
        #         if produs[1].day < value.day:
        #             self.expiration_date.insert(self.expiration_date.index(produs), (key, value))
        #             break
        #     else:
        #         self.expiration_date.append((key, value))

        #or

        for name, date in self.produse.items():
            self.expiration_date.append((name, date))

        self.expiration_date.sort(key=lambda date: date[1].day)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.expiration_date:
            raise StopIteration
        return self.expiration_date.pop()


shop = Shop("")
shop.add_product("Banana", datetime.datetime(2022, month=8, day=11))
shop.add_product("Kiwi", datetime.datetime(2022, month=8, day=13))
shop.add_product("Peach", datetime.datetime(2022, month=8, day=15))
shop.add_product("Peach2", datetime.datetime(2022, month=8, day=14))
shop.remove_product()
shop.write_to_file()
for produs in shop:
    print(produs)
