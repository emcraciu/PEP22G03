# lambda functions

def add_numbers(a, b):
    return a + b


print(add_numbers)
print("Normal function", add_numbers(10, 20))

add_numbers_ = lambda a, b: a + b  # we do not need the add_numbers_ variable here
print(add_numbers_)
print("Lambda function", add_numbers_(10, 20))


def apply_function(a, b, c):
    return a(b, c)


print(apply_function(add_numbers, 15, 16))
print(apply_function(add_numbers_, 15, 16))
print(apply_function(lambda a, b: a + b, 15, 16))

for i in range(100):
    print(apply_function(lambda a, b: a + b + i, 15, 16))

# map the function

result = map(lambda i: i + 5, [1,2,3,4])
print(result)
for i in result:
    print(i)

# filter the function

result = filter(lambda i: i - 1, [1,2,3,4])
print(result)
for i in result:
    print(i)
