# vom crea o lista de 5 iteme, printam fiecare item

# any_list = ["casa", 5 ,7.15, 8, "copac"]
# i = 0
# for any in any_list:
#     print(f" {any}")
#     i+= 1

# for i in any_list:
#     print(f'{i}')

# printeaza numerele de la 1 la 15
# for i in range(1, 16):
#     print(i)

# sa creem o lista cu minim 3 iteme iar unul dintre ele sa fie " group 16"
# sa adaugam un conditional statement => daca variabila este egala cu group 16 sa printam ceva

# element_list = [3.14, 2, True, "group 16"]
# for i in element_list:
#     print(i, type(i))
#     if i == "group 16":
#         print("Thats it.")

# for each_item in element_list:
#     print(each_item, type(each_item))
#     if each_item == "group 16":
#         print("Thats it.")

# sa creem un dictionare care sa contina un key group si valoarea 16
# daca cheia este grup si valoare 16
# sa printam ceva si sa avem un elsela final

# one_dict = {
#     'car' : 1,
#     'phone' : 2,
#     'group' : 16
# }
# print(one_dict)
# print(one_dict.get('group'))
# for each_item in one_dict:
#     if each_item == 'group' and one_dict[each_item] == 16:
#         print('Ok')
# else:
#     print('Finish')

# for x, y in one_dict.items():
#     print(f'x este {x} si y este {y}')
#     if x == 'group' and y == 16:
#         print('Passed.')
# else:
#     print('Finish.')

# sa creem un tuple cu 5 iteme, sa printem itereatorul si valoare in acelasi print

# an_tuple = ('Andrei', 345, 23.10, "course", 3.14)
# for i in range(len(an_tuple)):
#     print(f"Indexul este {i} iar valoarea este {an_tuple[i]}")

# for index, value in enumerate(an_tuple):
#     print(f"Indexul este {index} si valoare este {value}")

# creem o lista goala, adaugam in acea lista toate nr de la 1 la 99
# pentru fiecare iteratie sa adaugam nr care este itereat si contentul listei
# any_list = []
# for number in range(1, 100):
#     any_list.append(number)
#     print(f"{number} added to the list {any_list} ")

# facem un set cu minim 5 iteme
# sa printam indexul si itemul,
# daca lungimea set-ului este 5 sa iesim din loop.
# La final print "out of the loop"

# an_set = {"Andrei", 145, 4.14, "course", -5, 11, "yas", "bye-bye"}
# for index, value in enumerate(an_set):
#     if index == 5:
#         break
#     print(f"Index is {index}, item is {value}")
# else:
#     print("Out of the loop")

# printam un numar de la 2 la 150 folosind while loop

# count = 2
# while count <=150:
#     print(count)
#     count+=1

# o lista cu 5 iteme  si un string cu prenumele
# daca variabila este egala cu prenumele, continua
# daca nu printam ceva,
# inca un print "in loop"

# my_list = [0, True, "young", "David", 3.14]
# for item in my_list:
#     if item == 'David':
#         continue
#     else:
#         print(item)
#     print("in loop")

# o lista cu secventa fibonacci pana la 1000
# fibonacci_list = []
# a = 0
# b = 1
# sum = 0
# n = 0
# while sum <=1000:
#     fibonacci_list.append(sum)
#     n+=1
#     a = b
#     b = sum
#     sum = a + b
# print(fibonacci_list)