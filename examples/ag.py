# is

class Human:
    pass


class Student(Human):
    pass


# has
# class EngineGas:
#     def __init__(self, power):
#         self.power = power
#
#     def get_power(self):
#         return self.power
#
# class EngineElectric:
#     def __init__(self, power):
#         self.power = power
#
#     def get_power(self):
#         return self.power
#
# class Car:
#     def __init__(self, engine):
#         self.engine = engine
#
# c1 = Car(engine=EngineGas('120'))
# c2 = Car(engine=EngineElectric('142'))
#
# print(c1.engine.get_power())
# print(c2.engine.get_power())


from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    # def __init__(self, radius):
    #     self.radius = radius

    def perimeter(self):
        return 1

class Triangle(Shape):
    def perimeter(self):
        return 2

class Rectangular(Shape):
    def perimeter(self):
        return 3

shapes = [Circle(), Triangle(), Rectangular()]

for i in shapes:
    print(i.perimeter())


###############
class IsAdmin:
    def has_perm(self, request) -> bool:
        return True


# SOLID
