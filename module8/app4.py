# remove empty lines from text using filter

def remove_empty_lines(text:str):
    file = open(text, "r")
    result = file.read()
    return filter(lambda line:line, result.splitlines())

for i in remove_empty_lines("MyFile"):
    print(i)