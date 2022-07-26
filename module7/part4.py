# # static method
#
# class New_Car():
#     turbo = None
#
#     def __init__(self, hp: int):
#         self.hp = hp
#
#
# class Car():
#     turbo = False
#
#     def __init__(self, hp: int):
#         self.hp = hp
#
#     def add_turbo(self):
#         self.turbo = True
#         self.hp = self.calculate_hp(self.hp)
#
#     @staticmethod
#     def calculate_hp(initial_hp):
#         if initial_hp <= 50:
#             return initial_hp+(10*initial_hp)/100
#         else:
#             return initial_hp + (5 * initial_hp) / 100
#
#     @classmethod
#     def get_factory_turbo(cls):
#         print(cls.turbo)
#
#
#
# car = Car(100)
# car.add_turbo()
# print(car.hp)
# print(car.get_factory_turbo())
# print(car.__class__.turbo)
#
# new_car = New_Car(200)
# new_car.hp = Car.calculate_hp(new_car.hp)
# print(new_car.hp)


# class Car():
#     turbo = False
#     wheels = 0
#
#     def __init__(self, hp: int):
#         self.hp = hp
#         self.add_wheels()
#
#     def add_wheels(self):
#         self.wheels += 4
#
#     def calculate_hp(self):
#         if self.hp <= 50:
#             self.hp = self.hp + (10 * self.hp) / 100
#         else:
#             self.hp = self.hp + (5 * self.hp) / 100
#
#     def add_turbo(self):
#         self.turbo = True
#         self.calculate_hp()
#
#
# class Truck(Car):
#
#     def add_wheels(self):
#         self.wheels += 6
#
#     def add_turbo(self):
#         self.turbo = 2
#         self.calculate_hp()
#
#
# car = Car(45)
# print(dir(car))
# print("Car wheels", car.wheels)
# car.add_turbo()
# print("Car HP", car.hp)
#
# truck = Truck(100)
# print(dir(truck))
# print("Truck wheels", truck.wheels)
# truck.add_turbo()
# print("Truck HP", truck.hp)



class A():
    def abc(self):
        print('abc')

class B(A):
    def abc(self):
        print('bac')

class C(B, A):
    pass

a = A()
a.abc()

b = B()
b.abc()

c = C()
c.abc()