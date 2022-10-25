# """
# Structuri de date
#
# """
#
# colours_1 = ['verde']
# colours_2 = {}
# colours_3 = set()
# colours_4 = ()
# print(type(colours_1))
# print(type(colours_2))
# print(type(colours_3))
# print(type(colours_4))

# variabila_1 = list()
# variabila_2 = dict()
# variabila_3 = set()
# variabila_4 = tuple()
# print(type(variabila_1))
# print(type(variabila_2))
# print(type(variabila_3))
# print(type(variabila_4))

"""
ls prints the content of the folder
"""
# pentru lista fara paranteze se foloseste unpack
# my_group_is_awesome = ["apa", 2, False, 3.14, None]
# print(my_group_is_awesome)

# one_two_three_four_five = ["lmao", 18, False, 2.14, None, 715]
# print(one_two_three_four_five[::-1])
# python step

# an_not_so_empty_list = []
# an_not_so_empty_list.append("Yeah")
# an_not_so_empty_list.append(7.77)
# print(an_not_so_empty_list)

# another_list = ["item", 23, False, "two", 9.22]
# print(another_list)
# # pop sterge ultimul element, se poate folosi si index
# another_list.pop()
# print(another_list)

# simple_list = ["one", "one", 5, 9, False, "four", False, 3.15]
# print(simple_list.count("one"))
# 1 se numara impreuna cu True si 0 cu False

# list_forever = ["point", 4]
# print(list_forever[0])
# # list_forever[1] = "Georgica"
# # insert adauga fara a inlocui
# list_forever.insert(1, "Georgica")
# print(list_forever)

# last_list = ["one", "one", 5, 9, False, "four", False, 3.15]
# print(last_list)
# last_list.remove("one")
# print(last_list)

# my_fruit_list = ["banana", "peach", "apple"]
# my_vegetable_list = ["carrot", "mushroom", "tomato"]
# my_fruit_list.extend(my_vegetable_list)
# print(my_fruit_list)
# # o liste se poate inversa cu reverse sau step
# my_fruit_list.reverse()
# print(my_fruit_list)

# first_dict = {
#     "name" : "Jon",
#     "age" : "25",
#     "hair" : "blonde"
# }
# # print(first_dict)
# # print(type(first_dict))
# print(first_dict.keys())
# print(first_dict.values())
# print(first_dict["name"])

# second_dict = {
#     "age": "29",
#     "name": "Ion"
# }
# print(second_dict.get("namee", 45))
# # daca nu exista key ul se printeaza valoarea data
# print(second_dict.setdefault("name", "45"))
# print(second_dict)

# an_set = {"one", "four", 17}
# print(type(an_set))
# an_set.add("fourr")
# print(an_set)
# an_set.clear()
# print(an_set)

# another_set = {2, 17, 2.14}
# print(an_set.difference(another_set))

# 1. Sa facem un set din care sa scoatem un item fara nicio eroare si
# sa printam acel set
# 2. UN set, o variabila in care copiem valorile primului
# si printam variabila

# one_set = { 15, 22, 31.3, 3.14}
# one_set.remove(15)
# print(one_set)
#
# copy_of_set = one_set
# print(copy_of_set)


# a_tuple = ('one', 'four', 19, 'four')
# print(a_tuple.index('four'))
# b_tuple = (11, 25, 7.15)
# merged_tuple = a_tuple + b_tuple
# print(merged_tuple)

# 3. Se da un string cu minim 10 caractere, convertim stringul in tuple
# 4. Se da un tuple doar cu integer si float,
# printam minim si maxim si suma

# animal = "hippopotamus"
# print(tuple(animal))

# numbers = (10.1, 2, 3.14, 22, 81, 37.5)
# print(type(numbers))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

