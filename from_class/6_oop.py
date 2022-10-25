# # sa creem o clasa in care sa printam hello world apoi
# # sa o instantam
#
# class GroupSesion16:
#     print('Hello world!')
#
#
# object1 = GroupSesion16()


# create a class named Person with class var color, state
# and instance var wallet (float), compromised (bool)

# class Person:
#     color: str
#     state: bool
#     def __init__(self, wallet: float, compromised: bool):
#         self.wallet = wallet
#         self.compromised = compromised
#
# # wallet = 1000
# # compromised = False
# object2 = Person(wallet=1000, compromised=True)

# 3 create a class employee with two class var color(string), state(bool)
# create two methods which should print class variables,
# instantiate the class and call each method

# class Employee:
#     color = "White"
#     state = True
#     def print_color(self):
#         print(f"The color is {Employee.color}")
#     def print_state(self):
#         print(f"The state is {Employee.state}")
# object3 = Employee()
# object3.print_color()
# object3.print_state()

# sa creem o clasa numita base page
# Add 3 class variables, is displayed True, is default False,
# default timeout 3000
# Add 2 instances variables called number of tries, number of users
# Add method to print each instance var and each class var
# instantiate the class and all methods
# instantiate the class in an other object and call the methods

# class BasePage:
#     is_displayed: bool = True
#     is_default: bool = False
#     default_timeout: int = 3000
#     variable: None
#     value: None
#
#     def __init__(self, number_of_tries: int, number_of_users: int):
#         self.number_of_tries = number_of_tries
#         self.number_of_users = number_of_users
#
#     def custom_print(self, variable, value):
#         print(f"The value of variable  of: {variable} is: {value}")
#
#     def print_is_displayed(self):
#         self.custom_print(variable= "is_displayed", value= self.is_displayed)
#         # print(f"The base page is displayed: {self.is_displayed}")
#
#     def print_is_default(self):
#         print(f"The base page is default: {self.is_default}")
#
#     def print_default_timeout(self):
#         print(f"The base page timeout is: {self.default_timeout}")
#
#     def print_number_of_tries(self):
#         print(f"The number of tries is: {self.number_of_tries}")
#
#     def print_number_of_users(self):
#         print(f"The number of users is: {self.number_of_users}")
#
#
#
#
# class_base_page = BasePage(number_of_tries=3, number_of_users=1)
# class_base_page.print_default_timeout()
# class_base_page.print_is_default()
# class_base_page.print_is_displayed()
# class_base_page.print_number_of_tries()
# class_base_page.print_number_of_users()
# print("----------------------")
# another_object = BasePage(number_of_tries=5, number_of_users=2)
# another_object.print_number_of_users()
# another_object.print_number_of_tries()
# another_object.print_is_displayed()
# another_object.print_is_default()
# another_object.print_default_timeout()

# 4 create a new python file called class_imported_from_file
# create a class inside the new created class called ImportedClass
# add inside the class 2 instances variables called color and maker
# add one method inside the class which will print the 2 instances variables
# inside the same line
# import the class into oop_sesionsix.py
# intantiate the class and call the method

# from class_imported_from_file import ImportedClass
#
# object_imported = ImportedClass(color="blue", maker="Salomon")
# object_imported.print_self_default()
# object_imported.print_variables()
#
# object = ImportedClass(color="green", maker="Gioni")
# object.print_variables()

#--------------------------------------------
# smoke, sanity, regresion --- documentare
# smoke testare de baza
# sanity teste mai avansate fata de smoke
# regresion incorporeaza tot

# repo public pe github
# create a branch called group 16
# create a file homework sesion 6 in that file
# comenturi cu:
# what is boundering testing
# what is equivalance partition in testing
# create a pull request with the file added

# hints
# how to create a github repo, how to create a branch,
# source tree
# trimitem link catre acel pull request pe privat discord

# Equivalence partitioning is a software testing technique done before
# boundary testing and divides input data into equal partitions
# which function to obtain test cases or the individual test scenarios
# that developers perform in a system to determine if it functions correctly


# Boundary testing is a testing technique used to check errors
# at the boundaries or extreme ends of a given input domain

