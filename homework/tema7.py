""" OOP homework """
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from abc import ABC, abstractmethod


class GeometricForm(ABC):
    PI = 3.14

    @abstractmethod
    def area(self):
        raise NotImplementedError


class Square(GeometricForm):
    __side = 0

    def __init__(self, side: float):
        self.__side = side

    @property
    def side(self):
        return self.__side

    @side.getter
    def side(self):
        print(f'Getter: Value of side is {self.__side}')
        return self.__side

    @side.setter
    def side(self, new_value_of_side: float):
        print(f'Setter: New side value is {new_value_of_side}')
        self.__side = new_value_of_side

    @side.deleter
    def side(self):
        print('Deleter: side deleted')
        self.__side = None

    def area(self):
        square_area = self.__side * self.__side
        print(f'Square area is {square_area}')
        return square_area

    @staticmethod
    def describe():
        print('Most likely I have corners')


class Circle(GeometricForm):
    __radius = 0

    def __init__(self, radius: float):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.getter
    def radius(self):
        print(f'Getter: Radius value is {self.__radius}')
        return self.__radius

    @radius.setter
    def radius(self, new_value_of_radius: float):
        print(f'Setter: New radius value is {new_value_of_radius}')
        self.__radius = new_value_of_radius

    @radius.deleter
    def radius(self):
        print('Deleter: radius deleted')
        self.__radius = None

    def area(self):
        circle_area = self.PI * self.__radius * self.__radius
        print(f'Circle area is {circle_area:.2f}')
        return circle_area

    @staticmethod
    def describe():
        print('I dont have corners')


square_object1 = Square(side=1.99)
square_object1.side = 2
square_object1.side
del square_object1.side
square_object1.side
square_object1.describe()
square_object1.side = 3
square_object1.area()
print('---------------------------')
circle_object = Circle(radius=2.01)
circle_object.radius = 5
circle_object.radius
del circle_object.radius
circle_object.radius
circle_object.describe()
circle_object.radius = 1.5
circle_object.area()

# Tema clasa
# I. Descrierea pilonilor OOP
# 1. Inheritance- refers to the fact that a class child will inherit
# the methods and the attributes inside the class parent.
#  2. Polymorphism- refers to methods/functions with the same name
#   but have different form.
#  3. Abstraction- helps the programmer hide the process from the user so
#  the user knows what it is done but not how.
#  Therefore, an abstract class contains the pattern and the logic that will
#  be implemented in the child classes.
#  4. Encapsulation- refers to bundling data and methods within a single unit.
#  Also using encapsulation we can hide an object’s internal representation
#   from the outside.

# II. create a class called Person, inside the class person cu incapsulation patern
# add two class variables called hair, is_alive(bool),
# patru metode care: 1. seteaza culoarea parului,
# 2. seteaza bool
# 3. get hair color
# 4. get alive
# initiem clasa, apelam metodele


# class Person:
#     __hair_color: str = 'brown'
#     __is_alive: bool = True
#
#     def set_color(self, new_color):
#         print(f"Setter: The new hair color is: {new_color}")
#         self.__hair_color = new_color
#
#     def get_color(self):
#         print(f"Getter: The hair color is: {self.__hair_color}")
#         return self.__hair_color
#
#     def set_status(self, is_alive: bool):
#         print(f"Setter: The person is alive: {is_alive}")
#         self.__is_alive = is_alive
#
#     def get_status(self):
#         print(f"Getter: The person is alive: {self.__is_alive}")
#         return self.__is_alive
#
# human = Person()
# human.get_color()
# human.set_color(new_color='grey')
# human.get_color()
# human.get_status()
# human.set_status(is_alive=False)
# human.get_status()
