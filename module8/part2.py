# Iterator

class MyNumber(int):

    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return MyIterator(self.number)


class MyIterator():

    def __init__(self, number: int):
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        if not self.number:
            raise StopIteration
        self.number -= 1
        return self.number

my_number = MyNumber(15)

print('result',  my_number + 3)

for i in my_number:
    print(i)


# my_str = "abc"
# print(my_str.__iter__())
# print(my_str.__iter__().__iter__())

# class MyShop:
#
#     def __int__(self):
#         self.products = {}
#
#     def add_products(self):
#         self.products['x'] = 'y'
#
# shop = MyShop()
# for product in shop:
#     print(product)