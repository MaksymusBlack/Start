##    Модуль 2 - 2

# is_active = bool(input("Is the user active? "))
# is_admin = bool(input("Is the user administrator? "))
# is_permission = bool(input("Does the user have access? "))

# access = None
# if is_admin :
#     access = True
# elif is_active and is_permission :
#     access = True
# else:
#     access = False

# print(access)

##    
# work_experience = int(input("Enter your full work experience in years: "))

# if work_experience > 1 and work_experience <=5:
#     developer_type = "Middle"
# elif work_experience == 1:
#     developer_type = "Junior"
# else:
#     developer_type = "Senior"

# print(developer_type)

## Модуль 2 - 4

# num = int(input("Enter a number: "))

# if num > 0:
#     if num %2 == 0:
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"

# print(result)


## Модуль 2 - 7                            (Було складно)
# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# while num > 0:
#     sum = sum + num
#     num = num - 1

# print(sum)


## Модуль 2 - 8

# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for i in message:
#     if i == search:
#         result = result + 1

# print(result)


## Модуль 2 - 9              (Дуже складноб бо багато тупив)

# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))

# gcd = first if first < second else second

# while True:
#     if first % gcd == 0 and second % gcd == 0:
#         break
#     else:
#         gcd -= 1
    
# print(gcd)
    


## Модуль 2 - 10     

# num = int(input("Enter integer (0 for output): "))
# sum = 0

# while num != 0:
#     for i in range(num + 1):
#         sum += i
#     num = int(input("Enter integer (0 for output): "))

# print(sum)


# sum = 0
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if num == 0:
#         break
#     for i in range(num + 1):
#         if i % 2 == 1:
#             continue
            
#         sum = sum + i

# print(sum)


##   Модуль 2 - 13 (Дичиииина) ЖЖЕЕЕЕЕЕСТЬ!!!!!


# message = input("Enter a message: ")
# offset = int(input("Enter the offset: "))
# encoded_message = ""
# for ch in message:    
#     if ord(ch) >= 65 and ord(ch) <= 90: 
#         pos = ord(ch) - ord('A')
#         pos = (pos + offset) % 26
#         new_char = chr(pos + ord("A"))
#         encoded_message = encoded_message + new_char
#     if ord(ch) >= 97 and ord(ch) <= 122:
#         pos = ord(ch) - ord('a')
#         pos = (pos + offset) % 26
#         new_char = chr(pos + ord("a"))
#         encoded_message = encoded_message + new_char   
#     if ord(ch) <= 65:
#         encoded_message = encoded_message + ch
    
# print(encoded_message)


# ##   Модуль 2 - 15  Невже я це написав аааааааааааааааа

