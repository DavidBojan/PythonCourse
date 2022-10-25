# 1. create a function witch will print hello world
# def hello_world():
#     print("Hello world!")
#
#
# hello_world()

# 2. create a function witch have a parameter user and it prints Hello, user!
# def hello_user(user):
#     print(f"Hello, {user}!")
#
#
# hello_user(user="John")

# 3. create a function with a parameter user and a parameter age
# using assert for the name to be an expected name and age greater than 18
# also print the expected
# def verify_user_age(user, age: int):
#     assert user == "John", f'User expected: John, instead got {user}.'
#     assert age >= 18, f'Age expected: greater than 18, got: {age}.'
#     print(f"User {user} is over 18 years old.")


# verify_user_age(user="Andy", age=17)
# verify_user_age(user="John", age=18)

# 4. create a function with 3 parameters: user, age, hair
# for age, default 25
# print all parameters
# use the same function and change the age to 35
# def verify_user_age_hair(user, hair, age=25):
#     print(f"User {user} is {age} years old and has {hair} hair.")
#
#
# verify_user_age_hair(user="Andy", hair="brown")
# verify_user_age_hair(user="Andy", hair="grey", age=35)

# 5. create a function with 3 parameters integers
# return their sum, print sum
# def parameters_sum(one: int, two: int, three: int):
#     sum_of = one + two + three
#     return sum_of
#
#
# print(parameters_sum(one=2, three=1, two=3))

# 6. function with infinite arguments
# print every argument
# def inf_arg(*args):
#     print(type(args))
#     for i in args:
#         print(i)
#
#
# inf_arg(22, True, "Yep", 16, 23, 90, False, 15, "Tango")

# homework: function with infinite keyword arguments
# **kwargs
# Describe the function and the **kwargs
# Every parameter to be added in a list
# return the list, with type(list)
# hint: type hint
# assert len(list) > 0, expected greater than 2

def multiple_keyword_args(**kwargs):
    """This function will use **kwargs to create a list
    with multiple keywords and arguments"""
    assert len(kwargs) >= 2, f"Expected 2 or more elements, got {len(kwargs)} element/s"
    return type(kwargs), f"List of keyword args: {kwargs}"


print(multiple_keyword_args(one="1", two="2", three="3"))
