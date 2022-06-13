# get text from user and print it reversed

# 1
print("Astazi ma duc la \"facultate\"")
print("/*\/*\*/*\/*\\", "Python", "\./\./\./\./", sep="\n")
print("P\ty\tt\th\to\tn")
var = input('Textul este:')
print(var[::-1])

# 2
user_name = input("introduceti nume utilizator:")
age = input("introduceti varsta:")
print("Cum te numesti?", user_name)
print("Ce varsta ai?", age)
print(f"Ceau Ana! Te-ai nascut in {2022 - int(age)}")

# 5
user = input("Numele de utilizator este:")
user = bool(user == user[::-1])
print(user)

# 6
# a) Hello_Python
text = "Hello Python"
print(text[:5], "_", text[6:], sep="")

# b) Hello Python.
print('Hello', 'Python', end='.')

# c) HelloHelloHelloHello
text = "Hello Python"
print(text[:5] * 4)

# 7
a = 5.
b = 5
c = "ana"
print(hex(id(a)), type(a))
print(hex(id(b)), type(b))
print(hex(id(c)), type(c))
