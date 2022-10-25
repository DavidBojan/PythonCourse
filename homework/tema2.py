"""
1. Conditionalul if else se foloseste pentru a
 controla modul in care se desfasoara codul
"""

# 2
# x = int(input("Type a number x: "))
# print(f'{x} is an natural number.') if x > 0 else print(f'{x} isn\'t an natural number.')

# 3
# x = int(input("Type a number x: "))
# if x > 0:
#     print('Positive number.')
# elif x == 0:
#     print('Neutral number.')
# else:
#     print('Negative number.')

# 4
# x = int(input("Type a number x: "))
# if -2 < x < 13:
#     print(f'{x} is between -2 and 13')
# else:
#     print(f'{x} isn\'t between -2 and 13')

# 5
# x = int(input("Type a number x: "))
# y = int(input("Type a number y: "))
# difference = x - y
# if difference < 5:
#     print(f'{difference} difference is smaller than 5.')
# else:
#     print(f'{difference} difference is bigger than 5.')

# 6
# if not 5 < x < 27:
#     print(f'{x} is not between 5 and 27')
# else:
#     print(f'{x} is between 5 and 27')

# 7
# x = int(input("Type a number x: "))
# y = int(input("Type a number y: "))
# if x == y:
#     print("x and y are equal")
# elif x > y:
#     print("x is bigger than y")
# else:
#     print("y is bigger than x")

# 8
# x = int(input("Type a number x: "))
# y = int(input("Type a number y: "))
# z = int(input("Type a number z: "))
# if x == y == z:
#     print("equilateral triangle")
# elif x == y or y == z or x == z:
#     print("isosceles triangle")
# else:
#     print("Scalen triangle")

# 9
# letter = input("Input an char: ").strip().lower()
# if letter in ('a', 'e', 'i', 'o', 'u'):
#     print("Vowel")
# else:
#     print("Consonant")

# 10
# grade = int(input("Grade is: "))
# if 9 <= grade <= 10:
#     print("Grade is A")
# elif 8 <= grade < 9:
#     print("Grade is B")
# elif 7 <= grade < 8:
#     print("Grade is C")
# elif 6 <= grade < 7:
#     print("Grade is D")
# elif 4 < grade < 6:
#     print("Grade is E")
# elif 4 >= grade <= 1:
#     print("Grade is F")
# else:
#     print("Grade must be from 1 to 10")

# --------------- Exercitii optionale ----------

# 1
# x = int(input('Type x: '))
# if x > 999:
#     print('X has 4 digits.')
# else:
#     print('X has less than 4 digits')
# sau
# x = int(input('Type x: '))
# assert x > 0
# x = str(x)
# if (len(x)) >= 4:
#     print('X has 4 digits.')
# else:
#     print('X has less than 4 digits')
# sau
# import math
# x = int(input('Type x: '))
# digits = int(math.log10(x))+1
# if digits == 4:
#     print('X has 4 digits.')
# else:
#     print('X has more or less than 4 digits')

# 2 str(x).zfill(n) umple cu zerouri in partea stanga
# x = int(input('Type x: '))
# assert x >= 0
# x = str(x).zfill(6)
# print(str(x))
# if (len(x)) == 6:
#     print('x has 6 digits.')
# else:
#     print('x has more or less than 6 digits')


# 3
# x = int(input('Type x: '))
# if x == 0:
#     print('X equals zero')
# elif x % 2 == 0:
#     print('X is an even number')
# else:
#     print('X is an odd number')

# 4
# x = int(input('Type x: '))
# y = int(input('Type y: '))
# z = int(input('Type z: '))
# if x > z and x > y:
#     print("x is bigger")
# elif y > x and y > z:
#     print("y is bigger")
# elif z > y and z > x:
#     print("z is bigger")
# else:
#     print("the numbers are equal")

# 5
# x = int(input('Type x: '))
# y = int(input('Type y: '))
# z = int(input('Type z: '))
# if (x + y + z) == 180:
#     print("Valid triangle!")
# else:
#     print("Invalid triangle!")

# 6
# text = 'Coral is either the stupidest animal or the smartest rock'
# x = int(input('Type x: '))
# text_taiat = text[:-x]
# print(text_taiat)

# 7
# text = "Coral is either the stupidest animal or the smartest rock"
# print(text[:5] + text[-5:])

# 8
text = "Coral is either the stupidest animal or the smartest rock"
last_word = 'rock'
print(text[0:text.index(last_word)])

# 9
# text = str(input("Write an string: ")).strip()
# assert text[0].lower() == text[-1].lower()
# print(f"The first and the last letter of the String {text} are the same.")

# 10
# num = '0123456789'
# print('Even numbers: ' + num[0:-1:2])
# print('Odd numbers: ' + num[1::2])

# 11
# import random
# dice_roll = random.randint(1,6)
# dice_img = int(input("Type a number between 1 and 6: "))
# if 0 < dice_img < dice_roll:
#     print(f"Loser! You chose a smaller number, "
#           f"the dice was {dice_roll}, you typed {dice_img}.")
# elif 6 > dice_img > dice_roll:
#     print(f"Loser! You chose a bigger number, "
#           f"the dice was {dice_roll}, you typed {dice_img}.")
# elif dice_img == dice_roll:
#     print(f"Winner, winner, chicken dinner! "
#           f"The dice was {dice_roll}, you typed {dice_img}.")
# else:
#     print("The number is not in the requested range.")
