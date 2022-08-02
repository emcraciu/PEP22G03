# Generator

def generate_numbers():
    for i in range(3):
        yield i
    yield 20

my_gen = generate_numbers()
print(my_gen)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
# print(next(my_gen)) # - This last next call will result in StopIteration

