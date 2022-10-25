# 1
# def sum_of_2nmb(a, b):
#     return a + b
# print(sum_of_2nmb(2, 3))
# 2
# def nmb_even (c):
#     if c % 2 == 0:
#        return True
#     else:
#        return False
# print(nmb_even(4))
# 3
# def total_chrs(first_name, midle_name, last_name):
#     return len(first_name + midle_name + last_name)
# print("Number of characters: ", total_chrs("David", "Daniel", "Bojan"))
#  4
# def rectangle_area(a, b):
#     return a * b
# print("Rectangle area of L=6 si l=3 is: ", rectangle_area(6, 3))
#  5
# def circle_area(r):
#     return 3.14*r*r
# print("Circle area with radius 5 is: ", circle_area(5))
# 6
# def wanted_chr(words, x):
#     if words.count(x):
#         return True
#     else:
#         return False
# words = input("Type some words: ").upper()
# x = input("Insert an letter to be checked in the words: ").upper()
# assert len(x) == 1
# print(wanted_chr(words, x))
#  7
# def no_return_letters(any):
#     lower_let = 0
#     upper_let = 0
#     for l in any.replace(" ", ""):
#         if l.islower():
#             lower_let += 1
#         else:
#             upper_let += 1
#     print(f"Lower letters: {lower_let}")
#     print(f"Upper letters: {upper_let}")
# no_return_letters("SomE WorDs arOuNd")
# 8
# def a_very_positive_list(a_list):
#     positive_list = []
#     for index, number in enumerate(a_list):
#         if number >= 0:
#             positive_list.append(number)
#     return positive_list
# a_list = [1, 3, -5, -9, 11, 0, -23, 11, 12, 3, 2, 0]
# print(a_very_positive_list(a_list))
#  9
# def nmb_comparison(x, y):
#     if x > y:
#         print(f"{x} is bigger than {y}.")
#
#     elif y > x:
#         print(f"{y} is bigger than {x}.")
#     else:
#         print(f"{x} and {y} are equal.")
# nmb_comparison(-3, 4)
# nmb_comparison(0, 0)
# nmb_comparison(4, 3)
#  10
# def set_expension(nmb, set_nmb):
#     if nmb in set_nmb:
#         print("The number has not been added to the set. Already exists in the set")
#         return False
#     else:
#         set_nmb.add(nmb)
#         print("Number added to the set.")
#         return True
# an_set= {2, 5 , -9, 15, 22, 3.14, 9.11, 7.14, -3}
# print(set_expension(3, an_set))
# print(set_expension(2, an_set))
# ---------------Optionale-----------
# 1
# def days_of_month(month):
#     if month == 1:
#         return 'January has 31 days.'
#     if month == 2:
#         return 'February has 28 days.'
#     if month == 3:
#         return 'March has 31 days.'
#     if month == 4:
#         return 'April has 30 days.'
#     if month == 5:
#         return 'May has 31 days.'
#     if month == 6:
#         return 'June has 30 days.'
#     if month == 7:
#         return 'July has 31 days.'
#     if month == 8:
#         return 'August has 31 days.'
#     if month == 9:
#         return 'September has 30 days.'
#     if month == 10:
#         return 'October has 31 days.'
#     if month == 11:
#         return 'November has 30 days.'
#     if month == 12:
#         return 'December has 31 days.'
#     else:
#         return 'Chose an number between 1 and 12 which represent the month.'
# number_of_month = int(input("Type the number of the month to find out the days of the month: "))
# print(days_of_month(number_of_month))
# 2
# def calculator(x, y):
#     a = x + y
#     b = x - y
#     c = x * y
#     d = x / y
#     return print(f"Sum: {a} \n", f"Difference: {b} \n", f"Multiplication: {c} \n",
#                  f"Division: {d} \n", )
# calculator(10, 2)
#  3
def nmb_count(nmb_list):
    nmb_dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
        }
    key_list = nmb_dict.keys()
    values_list = nmb_dict.values()
    for index in key_list:
        if index == any(nmb_list):
             values_list+= 1
    return nmb_dict

a_list = [1, 3, 1, 5, 9, 7, 7, 5, 5, 0]
print(nmb_count(a_list))
#  4
# def max_of_three(x, y, z):
#     if x > y and x > z:
#         return print(f"{x} is bigger than {y} and {z} ")
#     if y > x and y > z:
#         return print(f"{y} is bigger than {x} and {z} ")
#     if z > x and z > y:
#         return print(f"{z} is bigger than {x} and {y} ")
# max_of_three(1, 2, 3)
# max_of_three(3, 2, 1)
# max_of_three(2, 1, 3)
#  5
# def sum_of_nmb(x):
#     nmb_sum = 0
#     for i in range(x+1):
#         nmb_sum+= i
#     return nmb_sum
# a = int(input("Give an number: "))
# print(f"The sum of the numbers is {sum_of_nmb(a)}")
# --------Optionale Bonus--------
# 1
# def commun_nmb(list1, list2):
#     list3 = []
#     for index in range(len(list1)):
#         if list2.count(list1[index]):
#             list3.append(index)
#     return list3
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# print(commun_nmb(list1, list2))
#  3
from datetime import datetime
# def date_and_time_ro():
# # Getting the current date and time
#     dt = datetime.now()
# # getting the timestamp
#     ts = datetime.timestamp(dt)
#     print("Date and time in Romania is:", dt)
#     # print("Timestamp is:", ts)
# date_and_time_ro()

# def date_and_time_china():
# # Timezone Name.
#     date_String = "23/Feb/2012:09:15:26 UTC +0800"
#     dt_format = datetime.strptime(date_String, '%d/%b/%Y:%H:%M:%S %Z %z')
#     print("Date with Timezone Name:", dt_format)
# # Timestamp
#     timestamp = dt_format.timestamp()
#     print("timestamp is:", timestamp)
# date_and_time_china()
# 4
# import datetime
# def day_till_birthday():
#     today = datetime.date.today()
#     someday = datetime.date(2022, 11, 3)
#     diff = someday - today
#     return print(f"{diff.days} days untill my birthday.")
# day_till_birthday()
# def day_till_christmas():
#     today = datetime.date.today()
#     someday = datetime.date(2022, 12, 25)
#     diff = someday - today
#     return print(f"{diff.days} days untill Christmas.")
# day_till_christmas()