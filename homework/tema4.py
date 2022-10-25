# exercitiul 1
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# print(cars)
# 1
# chosen_car = input("Select the favorite car from the list: ")
# assert cars.count(chosen_car) == True
# for n in range(len(cars)):
#     if cars.count(chosen_car):
#         print(f"My favorite car is {chosen_car}")
#         n+=1
#         break
# for car in cars:
#     if chosen_car == car:
#         print(f"My favorite car is {car}")
# n = 0
# while n <= len(cars):
#     if cars.count(chosen_car):
#         print(f"My favorite car is {chosen_car}")
#         n+=1
#         break
# 2
# for car in range(1, len(cars)-1):
#     cars[car] = cars[car].upper()
# else:
#     print(cars)
# 3
# wanted_car = "Mercedes"
# for wanted_car in cars:
#     if wanted_car == "Mercedes":
#         print("Found the wanted car. We have Mercedes!")
#         break
#     else:
#         print(f"Found {wanted_car}. Still searching...")
# 4
# for car in cars:
#     if car == "Trabant":
#         continue
#     elif car == "Lastun":
#         continue
#     else:
#         print(f"You may like the {car}.")
# 5
# old_cars = []
# for index, car in enumerate(cars):
#     if car == "Lastun":
#         old_cars.append(car)
#         cars[index] = "Tesla"
#     elif car == "Trabant":
#         old_cars.append(car)
#         cars[index] = "Tesla"
# print(old_cars)
# print(cars)
# 6
# car_prices = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000 }
# budget = 15000
# for key, value in car_prices.items():
#     # print(key)
#     # print(value)
#     if budget > value:
#         print(f"For a budget under {budget} euros you can choose the car {key}")
#     else:
#         pass
# 7
# numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# counter = 0
# for number in numbers:
#     if number == 3:
#         counter+=1
# print(f"The number 3 apears {counter} times.")
# 8
# total = 0
# for number in numbers:
#     total+= number
# print(f"The sum of the numbers is {total}")
# 9
# biggest = 0
# for number in numbers:
#     if number > biggest:
#         biggest = number
# print(biggest)
# 10
# for index, number in enumerate(numbers):
#     if number > 0:
#         numbers[index] = -abs(number)
# print(numbers)
# ----------------OPTIONALE---------------
# 1
# other_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# even_numbers = []
# odd_numbers = []
# positive_numbers = []
# negative_numbers = []
# for number in other_numbers:
#     if number % 2 == 0:
#         even_numbers += [number]
#         if number > 0:
#             positive_numbers += [number]
#         else:
#             negative_numbers += [number]
#     elif number % 2 != 0:
#         odd_numbers += [number]
#         if number > 0:
#             positive_numbers += [number]
#         else:
#             negative_numbers += [number]
#
# print("Positive numbers: ", positive_numbers)
# print("Negative numbers: ", negative_numbers)
# print("Odd numbers: ", odd_numbers)
# print("Even numbers: ", even_numbers)
# 2
# other_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# n = len(other_numbers)
# for i in range(n):
#     for j in range(1, n):
#         if other_numbers[j - 1] > other_numbers[j]:
#             (other_numbers[j - 1], other_numbers[j]) = (other_numbers[j], other_numbers[j - 1])
# print(other_numbers)
# 3
# import random
# secret_number = random.randint(1,30)
# guest_number = None
# while guest_number != secret_number:
#     guest_number = int(input(f"Choose a number between 1 and 30: "))
#     assert 30 >= guest_number >= 1
#     if guest_number > secret_number:
#         print("Secret number is smaller")
#     elif guest_number < secret_number:
#         print("Secret number is bigger")
# else:
#     print("congratulations! You guessed it!")
# 4
# pyramid = int(input("Choose a single digit number: "))
# # pyramid = str(pyramid)
# # size = len(pyramid)
# # assert size == 1
# # pyramid = int(pyramid)
# start = 1
# for i in range(pyramid):
#     for j in range(i+1):
#         print(start, end="")
#     start+=1
#     print("\n")
# 5
