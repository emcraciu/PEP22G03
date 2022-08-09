class PythonWriter:

    def __init__(self):
        self.file = open("my_script.py", "w")

    def get_input(self):
        var1 = ">>>"
        var2 = "..."
        var3 = "    "
        counter = 0
        in_try = False
        while True:
            x = input(f"{var1}")
            self.file.write(counter * "    " + x + "\n")
            try:
                if x[-1] == ":":
                    counter += 1
                    var1 = "..." + counter * var3
                if x.endswith("try:"):
                    in_try = True
                if x.endswith("finally:"):
                    in_try = False
            except IndexError:
                if counter == 0 and not in_try:
                    self.file.close()
                    return
                counter -= 1
                var1 = "..." + counter * var3


py = PythonWriter()
py.get_input()
