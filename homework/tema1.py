 # Exercitiul 1
# O variabila este un spatiu de memorie care pastreaza o anumita valoare

 # Exercitiul 2
# telefon = 'Xiaomi'
# model = 11
# frecventa = 2.4
# smart = True
# print(f'Telefonul este marca {telefon}, modelul {model}, '
#       f'are frecventa {frecventa} si este smart {smart}')

 # Exercitiul 3
# print(f'Tipul de data telefon este {type(telefon)}')
# print(f'Tipul de data model este {type(model)}')
# print(f'Tipul de data frecventa este {type(frecventa)}')
# print(f'Tipul de data smart este {type(smart)}')

 # Exercitiul 4
# frecventa = round(frecventa)
# print(f'Frecventa rotunjita este: {frecventa}')
# print(f'Tipul de data frecventa este {type(frecventa)}')

 # Exercitiul 5 ******* nepotriviri de tip
# print(f'Telefonul este marca {telefon}')
# print(f'Telefonul este modelul {model}')
# print(f'Telefonul are frecventa {frecventa}')
# print(f'Telefonul este smart {smart}')

 # Exercitiul 6
# numele = input(str('Introdu numele: '))
# prenumele = input(str('Introdu prenumele: '))
# print(f'Numele complet are {len(numele) + len(prenumele)} caractere')

 # Exercitiul 7
# lungimea = float(input('Introduceti lungimea: '))
# latimea = float(input('Introduceti latimea: '))
# print(f'Aria dreptunghiului este: {lungimea * latimea}')

# lungimea = input('Introduceti lungimea: ')
# latimea = input('Introduceti latimea: ')
# print(f'Aria dreptunghiului este: {float(lungimea) * float(latimea)}')

 # Exercitiul 8
# text = 'Coral is either the stupidest animal or the smartest rock'
# print(f'Cuvantul - the - apare de {text.count("the", 0, -1)} ori')

# # Exercitiul 9
# #Same?

 # Exercitiul 10
# text = '1324'
# assert text.isnumeric()
# print(text.isnumeric())

############### bonus ###################

 # 1
# string_impar = input('Scrie un string impar: ' )
# if len(string_impar) % 2 !=0:
#     #mijloc = round(len(string_impar)/2)
#     #print(len(string_impar),mijloc)
#     mijloc = len(string_impar)//2
#     print(f'Caracterul din mijloc este {string_impar[mijloc]}')
# else:
#     print('Stringul este par')

 # 2
# cuvant = input('Scrie un cuvant: ')
# palindrom = cuvant[::-1]
# assert cuvant == palindrom
# print(f'Cuvantul {cuvant} este palindrom.')

 # 3
# text = input('Scrie textul: ')
# lista = text.split()
# for i in range(0,len(lista)):
#     print(f'Variabila numarul {i} este {lista[i]}')

 # 4
# text = input('Scrie un string: ')
# first = text[0]
# last = text[-1]
# text_C = text[1:len(text)-1].replace(first, first.upper())
# print(first+text_C+last)

 # 5
# user = input('Introduceti user-ul: ')
# parola = input('Introduceti parola: ')
# parola_cenzurata = len(parola) * '*'
# print(f'Parola pt user-ul {user} este {parola_cenzurata} si are {len(parola)} caractere')
