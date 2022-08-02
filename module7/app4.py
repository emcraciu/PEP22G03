class Vehicle:
    pass

class Car(Vehicle):
    taking_corner1 = "not lening"
    headlights1 = "2 headlights"


class Bike(Vehicle):
    taking_corner2 = "is leaning"
    headlights2 = "1 headlights"


class ThreCar(Bike, Car):

    def __init__(self):
        self.__setattr__("taking_corner", self.taking_corner2)
        self.__setattr__("headlights", self.headlights1)
        # del Bike.headlights2
        # del Bike.taking_corner2
        # del Car.headlights1
        # del Car.taking_corner1



a = ThreCar()

print(a.__dir__())
print(a.headlights)
print(a.taking_corner)
