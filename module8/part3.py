# my_file = open("my_file.txt", "w")
# print(type(my_file))
# my_file.write("Hello World")
# my_file.close()

with open("my_file.txt", "w") as my_file:
    my_file.write("Hello World 1")


my_file = open("my_file.txt", "r")
result = my_file.read()
print(result)

my_file = open("my_file.txt", "a")
my_file.writelines(["newline", 'new line 2'])
my_file.close()

my_file = open("my_file.txt", "ab")
print(type(my_file))
my_file.write(b"\n my file \n")



