## Завдання 6


# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     else:
#         a = (length - len(string)) // 2
#         space = (" ")
#         for i in range(a):
#             if i:
#                 space = space + " "

#         return  f"{space}{string}"



## Task 7

# def first(size, *comments):
#     print(size, comments)
#     return  size + len(comments)


# def second(size, **comments):
#         print(size, comments)
#         return size + len(comments)


## Task 8

# def cost_delivery(quantity, *number, discount = 0):
#     for number in range(quantity):
#         result = 5 + number * 2
#         if discount:
#             result = result - (result * discount)
#     return result

    
# def cost_delivery(quantity, *_, discount=0):
#     """Функція повертає суму за доставлення замовлення.

#      Перший параметр &mdash; кількість товарів в замовленні.
#      Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0."""

#     result = (5 + 2 * (quantity - 1)) * (1 - discount)
#     print(result)
#     return result
    


## Task 10

# def factorial(n):
#     if n < 2:
#         return 1  # Базовий випадок
#     else:
#         return n * factorial(n - 1)  # Рекурсивний випадок
        

# def number_of_groups(n, k):
#     C = factorial(n) / (factorial(n - k) * factorial(k))
#     print(C)
#     return int(C)

# number_of_groups(50, 7)


## Task 11
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    




