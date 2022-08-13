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
import time
import datetime


class expirationDate_Tracker:

    products = {}

    def __init__(self, day: float):
        self.day = datetime.datetime.now()

    def __iter__(self):
        return ProductIterator(self.products)

    def add_name(self, name):
        self.products[name] = name

    def add_expiration_date(self, name, expiration_date):
        day, month, year = expiration_date.split(" ")
        self.products[expiration_date] = int(day), month, int(year)
        print(self.products[name])

    def remove_Product(self, name):
        if self.products[name] < "13 Aug 2022":
            del self.products[name]


class ProductIterator():
    all_products = []

    def __init__(self, products: dict):
        self.products = products
        for product_name, info in self.products.items():
            print(product_name, info)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.all_products:
            raise StopIteration
        return self.all_products.pop()

    def write_to_file(self):
        with open('my_file.out', "w") as file:
            for products in self:
                file.write(str(products))



k = expirationDate_Tracker(time.time())
k.add_name("Banana")
k.add_expiration_date('Banana', "11 Aug 2022")

k.add_name("Orange")
k.add_expiration_date('Orange', "12 Aug 2022")

k.add_name("Kiwi")
k.add_expiration_date('Kiwi', "13 Aug 2022")

k.add_name("Apple")
k.add_expiration_date('Apple', "14 Aug 2022")

k.add_name("Peach")
k.add_expiration_date('Peach', "15 Aug 2022")



k.remove_Product('Orange')
k.remove_Product('Banana')
k.write_to_file()
