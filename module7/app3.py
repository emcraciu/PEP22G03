class Computer(object):

    def typing(self):
        print("It is typing...")

    def clicking(self):
        print("It is clicking...")

    def pixeling(self):  # in minus la Server
        print("It is pixeling...")

    def __init__(self, central_unit):
        self.central_unit = central_unit


class Laptop(Computer):
    def __init__(self):
        super().__init__("Tablet")

    def take_pictures(self):
        print("chees")


class Server(Laptop, Computer):
    pixel = True

    def __init__(self):
        #super(Server, self).__init__()
        super().__init__()


computer = Computer("Unitate Centrala")
laptop = Laptop()
print(laptop.central_unit)
delattr(Server,  "pixel")
server = Server()
# print(server.pixel) <- attribute deleted



