"""Tema 6	- OOP _ Clase & Obiecte"""


# 1
# import math
#
#
# class Circle:
#     """Class Circle"""
#     radius: int = None
#     color: str = None
#
#     def __init__(self, radius: int, color: str):
#         """Constructors """
#         self.radius = radius
#         self.color = color
#
#     def circle_descr(self):
#         """Method circle description"""
#         print(f"The color is {self.color}, the radius is {self.radius}")
#
#     def area(self, ):
#         """Method circle area"""
#         circle_area = math.pi * self.radius * self.radius
#         return circle_area
#
#     def diameter(self):
#         """Method circle diameter"""
#         diameter = self.radius / 2
#         return diameter
#
#     def circumference(self):
#         """Method circle diameter"""
#         circumference = 2 * math.pi * self.radius
#         return circumference
#
#
# circle_object = Circle(2, 'green')
# circle_object.circle_descr()
# print(f"Circle area is: {circle_object.area()}")
# print(f"Circle diameter is: {circle_object.diameter()}")
# print(f"Circle circumference is: {circle_object.circumference()}")
#
# 2
#
# class Rectangle:
#     """Class Rectangle"""
#
#     def __init__(self, lenght: float, width: float, color: str):
#         """Class constructors"""
#         self.lenght = lenght
#         self.width = width
#         self.color = color
#
#     def rectangle_descr(self):
#         """Rectangle description method"""
#          print(f"{self.color.capitalize()} rectangle "
#                f"with lenght: {self.lenght} and width: {self.width}")
#
#     def rectangle_area(self):
#         """Rectangle area method"""
#         area = self.lenght * self.width
#         return area
#
#     def rectangle_perimeter(self):
#         """Rectangle perimeter method"""
#         perimeter = 2 * (self.lenght + self.width)
#         return perimeter
#
#     def rectangle_color_change(self, new_color):
#         """Rectangle color change method"""
#         self.color = new_color
#
#
# rectangle_object = Rectangle(2.5, 5, 'red')
# rectangle_object.rectangle_descr()
# print(f"Rectangle area is: {rectangle_object.rectangle_area()}")
# print(f"Rectangle perimeter is: {rectangle_object.rectangle_perimeter()}")
# rectangle_object.rectangle_color_change('green')
# rectangle_object.rectangle_descr()
#
# 3
#
# class Employee:
#     """Class Employee"""
#
#     def __init__(self, first_name: str, last_name: str, salary: float):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary
#
#     def employee_descrp(self):
#         """Employee description method"""
#         print(f"Employee {self.first_name} has the salary: {self.salary}")
#
#     def complete_name(self):
#         """Complete name method"""
#         print(f"Complete name of the Employee: {self.first_name, self.last_name}")
#
#     def monthly_salary(self):
#         """Monthly salary method"""
#         monthly_salary = self.salary
#         return monthly_salary
#
#     def annual_salary(self):
#         """Annual salary method"""
#         annual_salary = self.salary * 12
#         return annual_salary
#
#     def salary_raise(self):
#         """Salary raise method"""
#         salary_raise = "7%"
#         raised_salary = self.salary * 1.07
#         pay_raise = raised_salary - self.salary
#         print(f"Salary raise of {salary_raise}\n"
#               f"Pay raise: {pay_raise:.2f}\n"
#               f"Final salary: {raised_salary}")
#
#
# emp_object = Employee('Alfie', 'Solomons', 2456)
# emp_object.employee_descrp()
# print(f"Employee complete name: {emp_object.complete_name()}")
# print(f"Monthly salary: {emp_object.monthly_salary()}")
# print(f"Annual salary: {emp_object.annual_salary()}")
# emp_object.salary_raise()
#
#  4
#
# class Account:
#     """Class Account"""
#
#     def __init__(self, iban: str, account_holder: str, balance: float):
#         self.iban = iban
#         self.account_holder = account_holder
#         self.balance = balance
#
#     def view_balance(self):
#         """View balance method"""
#         print(f"Account holder {self.account_holder} "
#               f"has the amount of ${self.balance} in account")
#
#     def debiting(self):
#         """Debiting the account"""
#         amount = float(input("Enter amount to be debited: "))
#         self.balance -= amount
#         return self.balance
#
#     def crediting(self):
#         """Crediting the account"""
#         amount = float(input("Enter amount to be credited: "))
#         self.balance += amount
#         return self.balance
#
#
# account_object = Account('RO49 AAAA 1B31 0075 9384 0000', 'Alfie Solomons', 31229.12)
# account_object.view_balance()
# account_object.debiting()
# account_object.crediting()
# account_object.view_balance()
#
# ----------------------Optionale----------
# 1
# from datetime import date
# from tabulate import tabulate
#
#
# today = date.today()
#
#
# class Bill:
#     """Class Bill"""
#
#     series = 'TST'
#
#     def __init__(self, number: int, product_name: str, quantity: int, piece_price: float):
#         self.number = number
#         self.product_name = product_name
#         self.quantity = quantity
#         self.piece_price = piece_price
#
#     def quantity_change(self, new_quantity: int):
#         """Quantity change method"""
#         self.quantity = new_quantity
#         return new_quantity
#
#     def price_change(self, new_pricce: float):
#         """Price change method"""
#         self.piece_price = new_pricce
#         return new_pricce
#
#     def name_change(self, new_name: str):
#         """Price change method"""
#         self.product_name = new_name
#         return new_name
#
#     def generate_bill(self):
#         """Generate bill method"""
#         total = self.piece_price * self.quantity
#         data = [[self.product_name, self.quantity, self.piece_price, total]]
#         table = tabulate(data, headers=['Product', 'quantity', 'piece_price', 'total'], tablefmt="github")
#         print(f"Bill series {self.series} number {self.number} \nDate: {today} \n{table}")
#         print("---------------------------------------------------------")
#
#
# bill_object = Bill(12, 'mouse', 5, 49.99)
# bill_object.generate_bill()
# bill_object.quantity_change(10)
# bill_object.price_change(40)
# bill_object.name_change('keyboard')
# bill_object.generate_bill()
#
# 2
#
# class Car:
#     """Class Car"""
#
#     make: str = 'Subaru'
#     actual_speed: float = 0
#     color: str = 'grey'
#     available_colors: set = {'blue', 'black', 'red', 'green', 'orange'}
#     matriculated: bool = False
#
#     def __init__(self, model: str, max_speed: float):
#         self.model = model
#         self.max_speed = max_speed
#
#     def description(self):
#         """ Car description method """
#         print(f"Make: {self.make} \n"
#               f"Model: {self.model} \n"
#               f"Actual speed: {self.actual_speed} \n"
#               f"Max speed: {self.max_speed} \n"
#               f"Color: {self.color} \n"
#               f"Matriculated: {self.matriculated} \n"
#               f"------------------------------------")
#
#     def matriculation(self):
#         """" Matriculation method"""
#         self.matriculated = True
#         return self.matriculated
#
#     def paint(self, new_color: str):
#         """ Painting the car method """
#         if new_color.lower() in self.available_colors:
#             self.color = new_color
#         else:
#             print(f"Color not available, choose one of these colors: {self.available_colors}")
#         return self.color
#
#     def accelerate(self, new_speed: float):
#         """ Accelerate method """
#         if new_speed < 0:
#             print("!!!! Error - negative speed !!!!")
#         elif new_speed > self.max_speed:
#             self.actual_speed = self.max_speed
#         else:
#             self.actual_speed = new_speed
#         return self.actual_speed
#
#     def brake(self):
#         """ Brake method """
#         self.actual_speed = 0
#         return self.actual_speed
#
#
# car_object = Car('XV', 220)
# car_object.description()
# car_object.matriculation()
# car_object.paint('green')
# car_object.accelerate(250)
# car_object.description()
# car_object.brake()
# car_object.description()
# car_object.accelerate(-20)
# car_object.paint('yellow')
# car_object.description()
#
# 3

class TodoList:
    """Todo list class"""

    todo: dict = {}

    def add_task(self, name: str, description: str):
        """" Adding a task to the dictionary"""
        self.todo.setdefault(name, description)

    def complete_task(self, name: str):
        """ Deleting the task from the dictionary """
        self.todo.pop(name)
        print(f"Task {name} has been complete.")
        print('----------------------------------------')

    def print_the_todo_list(self):
        """" Printing the todo list keys """
        for key, value in self.todo.items():
            print(key)
        print('-------------------------------------')

    def print_task_details(self, name: str):
        """ Task details """
        if name in self.todo.keys():
            print(f"Task {name} details: {self.todo.get(name)}")
            print('-------------------------------------------')
        else:
            answer = str(input(f"Do you want to add the task {name}? yes or no: "))
            if answer == 'no':
                print('Goodbye!')
                print('-------------------------------------------')
            elif answer == 'yes':
                description = str(input("Enter the task details: "))
                print('-------------------------------------------')
                self.todo.setdefault(name, description)



todo_object = TodoList()
todo_object.add_task('cleaning the pool', 'to do by 12 pm tomorrow')
todo_object.add_task('wash the car', 'today')
todo_object.add_task('cooking', 'starter and a main menu')
todo_object.print_the_todo_list()
todo_object.complete_task('wash the car')
todo_object.print_the_todo_list()
todo_object.print_task_details('cooking')
todo_object.print_task_details('cut the grass')
todo_object.print_the_todo_list()
