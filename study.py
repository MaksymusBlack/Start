# name = 'Oleg'
# hello_string = f"Hello, {name}!"
# print (hello_string, type (name))

# price = float (input ("Ціна:"))
# quantity = float (input ("Кількість:"))
# bill = f"З вас {price * quantity} uan"
# print (bill)

# a = int (input ())
# b = int (input ())
# c = int (input ())
# sum = a + b + c
# dit = a * b * c
# st = a ** (b - c)
# print (sum, dit, st)

# a = input('Введіть число:')
# a = int(a)
# if a > 0:
#     print('Число додатне')
# elif a < 0:
#     print("Число від'ємне")
# else:
#     print('Це число - нуль')

# result = None
# if result:
#     print(result)
# else:
#     print("Result is None, do something")

# some_data = None
# msg = some_data or "Не було повернено даних"
# print (msg)

# is_nice = True
# state = "nice" if is_nice else "not nice"
# print (state)

# name = input ("Ім'я:")
# age = int (input ("Вік:"))
# has_driver_licence = True

# if name and age >= 18 and has_driver_licence:
#     print(f"User {name} can rent a car")


# name = input("Ім'я:")
# age = input ("Вік:")
# hobby = input ("Хоббі:")
# state = f"My name is {name}, I am {age} and my hobby is {hobby}"
# print (state)

# x = int(input("X: "))
# y = int(input("Y: "))
# if x >= 0:
#     if y >= 0:               # x > 0, y > 0
#         print("Перша чверть")
#     else:                    # x > 0, y < 0
#         print("Четверта чверть")
# else:
#     if y >= 0:               # x < 0, y > 0
#         print("Друга чверть")
#     else:                    # x < 0, y < 0
#         print("Третя чверть")

# import math

# f = 0.5
# a = -2
# b = 7
# c = -6
# D = abs(math.pow(b, 2) - 4 * (a) * (c))
# x1 = ((-b) + math.pow(D, 0.5)) / (2 * a)
# x2 = ((-b) - math.pow(D, 0.5)) / (2 * a)
# print(D, x1, x1)

# while True:
#     number = input("number = ")
#     number = int(number)
#     while True:
#         print(number)
#         number = number - 1
#         if number < 0:
#             break

    
# import math

# RADIUS = 6371.01

# lat1 = 50.45
# lon1 = 30.523

# lat2 = 51.5072
# lon2 = -0.1275

# distance = RADIUS * math.acos(math.sin(math.radians(lat1)) * math.sin(math.radians(lat2)) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(math.radians(lon1 - lon2)))
# print(distance)

# RADIUS = 6371.01

# lat1 = math.radians(50.45)
# lon1 = math.radians(30.523)

# lat2 = math.radians(51.5072)
# lon2 = math.radians(-0.1275)

# distance = RADIUS * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))
# print(distance)

# a = int(input())
# print(f"The next number for the number {a} is {a + 1}")
# print(f"The previous number for the number {a} is {a - 1}")

# import decimal

# a = int(input("Основа трикутника: "))
# b = int(input("Висота трикутника: "))
# c = round(0.5 * a * b, 2)

#Варіант через список
# three = [int(input("Основа трикутника: ")), int(input("Висота трикутника: ")) ] 
# c = round(0.5 * three[0] * three[1], 2)

# print(c)


# def task_two():
#     n = int(input("Enter your n: "))
#     t = str(n)
#     t2 = t + t
#     t3 = t + t + t
#     sum = n + int(t2) + int(t3)
#     print(sum)
# task_two()
# task_two()
# task_two()


# def print_max(a, b):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'дорівнює', b)
#     else:
#         print(b, 'максимально')

# print_max(3, 4)  # пряма передача значень

# x = 5
# y = 7
# print_max(x, y)  # передача змінних у якості аргументів

# def factorial(n):       
#     if n >= 5:
#         return 5
#     else:
#         return n * factorial(n + 1)

# print(factorial(1))    # 120

# data = [] #список

# for i in range(10):
#     value = int(input("Enter your number: "))
#     data.append(value)

# print(data)

#Словник
# user = {"name": "Maksym", "age": 32}

# info = {
#     "city": "Sudak",
#     "index": "98000"
# }

# user.update(info)


# print(user)



#Task 6

# n = str(179)
# # num_str = repr(n)
# # last_digit_str = num_str[-1]
# # last_digit = int(last_digit_str)

# print(last_digit)

odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(i ** 2)