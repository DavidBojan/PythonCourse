""" exercitiul 1, 2 """
# note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
# print(note_muzicale)
# note_muzicale = note_muzicale[::-1]
# print(note_muzicale)
# note_muzicale.reverse()
# print(note_muzicale)
# print(f"Do apare de {note_muzicale.count('do')} ori")

# exercitiul 3, 4, 5, 6, 7
# a_list = [3, 1, 0, 2]
# b_list = [6, 5, 4]
# a_list.extend(b_list)
# print(sorted(a_list))
# # second variant
# a_list = [3, 1, 0, 2]
# b_list = [6, 5, 4]
# merged = a_list + b_list
# print(merged)
#
# merged.sort()
# print(merged)
# merged.pop(0)
# print(merged)

# a_list.sort()
# print(a_list)

# print(a_list)
# if not a_list:
#     print("The list is empty")
# else:
#     print("The list is not empty")
# a_list.clear()

# exercitiul 8. 9. 10. 11

# dict1 = {
#     'Ana' : 8,
#     'Gigel' : 10,
#     'Dorel' : 5
# }
# Elevii = dict1.keys()
# print(Elevii)
# print(f"Ana a luat nota {dict1.get('Ana')}")
# print(f"Gigel a luat nota {dict1.get('Gigel')}")
# print(f"Dorel a luat nota {dict1.get('Dorel')}")
# nota_corectata = {"Dorel" : 6}
# dict1.update(nota_corectata)
# print(f"Dorel a luat nota {dict1.get('Dorel')}")
# dict1.pop("Gigel")
# dict1.setdefault("Ionica", 9)
# print(dict1)

# exercticiul 12, 13, 14 ,15
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# zile_sapt.add('luni')
# print(zile_sapt)
# if weekend.issubset(zile_sapt):
#     print("Weekend is an subset.")
# else:
#     print("Weekend is not an subset")
# print(zile_sapt.difference(weekend))
# print(zile_sapt.intersection(weekend))

# exercitii optionale
#
# players = [1, 7, 11, 4, 20]
# print(players)
# max_change: int = 0
# for trials in range(1, 6):
#     print("-----------------------------------------------------")
#     player_on = int(input("Chose the player you want to change: "))
#     player_given = int(input("Chose a new player: "))
#     assert player_given != player_on
#     assert player_given > 0
#     assert player_on > 0
#     if player_on in players:
#         players.remove(player_on)
#         players.append(player_given)
#         max_change += 1
#         if max_change < 3:
#             print(f"{player_given} has entered, {player_on} is out,\n"
#                   f" Maximum 3 changes: {max_change}/3,\n"
#                   f" Maximum 5 trials: {trials}/5.")
#         elif max_change == 3:
#             print("Maximum changes reached!")
#         print(players)
#     elif player_on not in players:
#         if trials < 5:
#             print("The change cannot be done, the player is not in the field,\n"
#                   f"Maximum 3 changes: {max_change}/3,\n"
#                   f"Maximum 5 trials: {trials}/5. ")
#         elif trials == 5:
#             print("Maximum trials reached!")
#         print(players)
