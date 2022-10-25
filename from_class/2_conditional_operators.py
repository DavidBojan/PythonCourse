# Today we will learn
# if, elif, else

# myName = input("""- What is your name?
# - """).strip().lower()
# assert len(myName) > 1
# # mai exista variata de a elimna spatiile prin replace
# if myName == 'David':
#     print(f'Your name is {myName}')
# elif myName == 'david':
#     print(f'*'*50)
# elif myName == 'paula':
#     print(f'_'*100)
# #    assert len(myName) == 5
# else:
#     print(f'- Expected David, input was {myName}')

#
# myAge = int(input("What is your age? "))
# print(myAge) if myAge == 30 else print(f"You are too young!")
# if myAge < 2 and myAge < 5:
#     print(f"The human is too young!")
# elif myAge > 2 and myAge <5:
#     print(f'The human is younger!')

# 0 - your age cannot be zero; 1 si 14 - minor; 14 18 - milenial
# if myAge == 0:
#     print('Your age can\'t be 0.')
# elif 1 <= myAge < 14:
#     # myAge >= 1 and myAge < 14:
#     print('You are a minor')
# elif 14 <= myAge < 18:
#     # myAge >= 14 and myAge < 18:
#     print('You are a milenial')
# else:
#     print('You\'re an adult! wow')

# isCursed = 'summer'
# if isCursed != 'summer':
#     pass
# else:
#     print('something something')

# TEMA BOOONUUUUSSSS

# string de tip int de la user 'what is the price?'
# un assert ca lenght de input este mai mare decat 1 si mai mic decat 11
# daca nr este par atunci 'you ve given an even number'
# daca nr este impar 'price is odd'

# price = input('What is the price? ')
# assert 1 < len(price) < 11
# price = int(price)
# if price % 2 == 0:
#     print('You\'ve given an even number')
# else: print('The price is an odd number')

# o variabila la care ii atribuim o valoare random intre 2 si 200
# printam variabila
# import random
#
# price = random.randint(2,200)
# print(price)

# install pylint
