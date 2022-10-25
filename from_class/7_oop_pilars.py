# 1 create a class named person which has a method print
# value for index, method which takes an argument called index(int)
# inside that method add a list with five integers,
# add a try except and the except should catch index error toghether
# which will show the index and the error
# Add also a cod logic(print) which will run even tho the cod will
# enter the exception. Instanciete the class and call the method

# class Person:
#
#     def print_value_for_index(self, index: int):
#         """Printing value for index"""
#         integers = [0, 3, 12, 9, 17]
#         try:
#             print(f"Returning value from list {integers[index]} "
#                   f"and the index is {index}")
#         except IndexError as index_error:
#             # print(f"index: {index} and {index_error}")
#             raise IndexError
#         finally:
#             print(f"The value of index {index} is {integers[index]}")
#
#
# person_object = Person()
# person_object.print_value_for_index(index=10)
# person_object.print_value_for_index(index=6)

# 2 Create a class called Person which will have a method print_hello_world
# which will print 'hello world'
# create another class called Employee which will enherit from Person
# inside the class Employee create a method called print_hello_name
# which will take an argument(str), default value 'Mr. Robot'
# Instantiate the class employee and call the method world and hello name

# class Person:
#     """Class Person"""
#     @staticmethod
#     def print_hello_world():
#         """ Print hello world """
#         print('Hello world!')
#
#
# class Employee(Person):
#     """ CLass Employee enheriting class Person """
#     @staticmethod
#     def print_hello_name(name: str = 'Mr. Robot'):
#         """ Print name """
#         print(f"Hello {name}")


# este posibila mostenirea multipla dar nu recomandata
# class Employer(Employee):
#     pass


# angajatul = Employee()
# angajatul.print_hello_world()
# angajatul.print_hello_name()
# angajatorul = Employer()
# angajatorul.print_hello_name(name='Jean')


# 3 Create a class name BasePage which has a methjod called print_hello_word
# which will print 'Hello world'
# create another class called LogginPage which inherits from base_page and
# has a method print_hello_Word
# inside the mwthod we will prin Hello Universe
# INitiate login_page and call method
# --------Polimorfismul se realizeaza prin overwrite sau overload-------
# overwrite = se suprascrie metoda
# overload = mai multe metode cu acelasi nume dar continut diferit

# class BasePage:
#     """Class base page"""
#     def print_hello_word(self):
#         """Class print hello word"""
#         print('Hello World!')
#
#
# class LoginPage(BasePage):
#     """Class Login Page"""
#     def print_hello_word(self):
#         print("Hello Universe!")
#
#
# acces_to_page = LoginPage()
# acces_to_page.print_hello_word()

# Create a class called BasePage and one method called print_hello_world
# which must be implemented by all classes
# create a class settings_page which enherites from BasePage
# inside the settings class create a method that will bring the sum of
# two arguments(int)
# initiate the class and call the method
#
# from abc import ABC, abstractmethod
#
#
# class BasePage(ABC):
#     """Class Base Page"""
#     @abstractmethod
#     def print_hello_world(self):
#         """ Print hello world"""
#         print('Hello world!')
#         raise NotImplementedError('Method not implemented')
#
#
# class SettingsPage(BasePage):
#     """ Class Settings Page"""
#
#     @staticmethod
#     def sum_of_arguments(x: int, y: int):
#         """ Sum of two arguments(int) """
#         sum_of = x + y
#         print(f"Sum of {x} + {y} = {sum_of}")
#
#     def print_hello_world(self):
#         print('boohoo')
#
# an_object = SettingsPage()
# an_object.sum_of_arguments(x=4, y=4)

# incapsulation

# class Car:
#     __running = False
#     __model = 'Toyota'
#
#
#     def set_running_state(self, state):
#         self.__running = state
#
#     def set_model(self, model):
#         self.__model = model
#
#     def get_running_state(self):
#         return self.__running
#
#     def get_model(self):
#         return  self.__model
#
#
# obj_car = Car()
# obj_car.set_model('Hyundai')
# obj_car.set_running_state(True)
# print(obj_car.get_model())
# print(obj_car.get_running_state())

# 1. tema descrierea pilonilor OOP
# 2. create a class called Person, inside the class person cu incapsulation patern
# add two class variables called hair, is_alive(bool),
# 4 metode care 1. seteaza culoarea parului,
# 2. seteaza bool
# 3. get hair color
# 4. get alive
# initiem clasa, apelam metodele
