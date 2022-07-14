# generic problems

"""
Create application that will ask the user for python input and format the input prompt as needed.

"""

var1 = ">>>"
var2 = "    "
counter = 0
in_try = False
while True:
    inp = input(f"{var1} ")
    try:
        if inp[-1] == ":":
            counter += 1
            var1 = "..." + counter * var2
        if inp.endswith("try:"):
            in_try = True
        if inp.endswith("finally:"):
            in_try = False
    except IndexError:
        if counter == 0 and not in_try:
            quit()
        counter -= 1
        var1 = "..." + counter * var2
