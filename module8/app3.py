# write python code to file

class PythonWriter:

    def __init__(self):
        self.file = open("my_script.py", "w")

    def get_input(self):
        while True:
            input(">>>")

py = PythonWriter()
py.get_input()
