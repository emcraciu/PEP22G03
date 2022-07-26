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
