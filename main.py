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

x = int(input("X: "))
y = int(input("Y: "))
if x >= 0:
    if y >= 0:               # x > 0, y > 0
        print("Перша чверть")
    else:                    # x > 0, y < 0
        print("Четверта чверть")
else:
    if y >= 0:               # x < 0, y > 0
        print("Друга чверть")
    else:                    # x < 0, y < 0
        print("Третя чверть")