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

class Shop:
    """product class"""

    products = {}


    def __init__(self, day: float):
        self.day = datetime.datetime.now()

    def __iter__(self):
        return ShopIterator(self.products)

    def add_prod(self, name):
        """add products class"""
        self.products[name]=name


    def add_exp_date(self, name, exp_date):
        day, month, year = exp_date.split(":")
        # self.products[name].append((int(day), month, int(year)))
        print(self.products[name])

    def remove_product(self, name):
       del self.products[name]


class ShopIterator():
    all_products = []

    def __init__(self, products: dict):
        self.products = products
        for product_name, inf in self.products.items():
            print(product_name, inf)



    def __iter__(self):
        return self

    def __next__(self):
        if not self.all_products:
            raise StopIteration
        return self.all_products.pop()


p = Shop(time.time())
p.add_prod('Banana')
p.add_exp_date('Banana', "11:Aug:2022")

p.add_prod('Orange')
p.add_exp_date('Orange', "12:Aug:2022")

p.add_prod('Kiwi')
p.add_exp_date('Kiwi', "13:Aug:2022")

p.add_prod('Apple')
p.add_exp_date('Apple', "14:Aug:2022")

p.add_prod('Peach')
p.add_exp_date('Peach', "15:Aug:2022")

p.remove_product('Banana')
p.remove_product('Orange')


for prod in p:
    print(prod)

