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

    def remove_product(self, produs, data_expirare):
        """Metoda care sterge produsele expirate"""
        zi, luna, an = data_expirare.split(" ")
        now = datetime.datetime.now()
        date_time_str = now.strftime("%d %m %Y")
        print(date_time_str)
#        if int(date_time_str[0:1]) > self.

    def write_to_file(self):
        """Metoda care scrie datele in fisier"""
        with open('my_file.out', "w") as file:
            for product in self:
                file.write(str(product))

class ShopIterator():
    """Clasa iteratorului"""

    expiration_date = []

    def __init__(self, produse: dict):
        self.produse = produse
        for name, date in self.produse.items():
            self.expiration_date.append((name, date))

    def __iter__(self):
        return self

    def __next__(self):
        if not self.expiration_date:
            raise StopIteration
        return self.expiration_date.pop()

shop = Shop("")
shop.add_product("Banana", "11 08 2022")
shop.add_product("Kiwi", "13 08 2022")
shop.add_product("Peach", "15 08 2022")
shop.remove_product('Peach', '13 08 2022')
print(shop.produse)
