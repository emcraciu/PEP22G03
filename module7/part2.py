# class for store

# - open shop with some products
# - add products
# - remove products

class Shop:

    def __init__(self, products):
        self.products = products

    def add_product(self, name, quantity):  # <- fix add
        self.products[name] = quantity

    def remove_product(self, name):
        del self.products[name]

my_shop = Shop({'camera': 5, 'mouse': 2})
print(my_shop.products)
my_shop.add_product('keyboard', 3)
print(my_shop.products)
my_shop.remove_product('mouse')
print(my_shop.products)
my_shop.add_product('keyboard', 2)
print(my_shop.products)