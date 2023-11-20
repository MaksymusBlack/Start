##    Task 1

# def amount_payment(payment):
#     sum = 0
#     for i in payment:
#         if i > 0:
#             sum = sum + i                 
#     print(sum)    
#     return sum
    

## Task 2

# def prepare_data(data):
#     new_data = sorted(data)
#     new_data.pop(0)
#     new_data.pop()
#     return new_data


## Task 3

# def format_ingredients(items):
    
#         if len(items) == 1:
#             return items[0]
#         elif len(items) == 0:
#             return ""
#         else:
#             formatted_ingredients = ", ".join(items[:-1])
#             formatted_ingredients += " and " + items[-1]
#             print(formatted_ingredients)
#             return formatted_ingredients



## Task 4

# def get_grade(key): 
#     items = {'F':1, 'FX':2, 'E':3, 'D':3, 'C':4, 'B':5, 'A':5}
#     if key in items:        
#         print(items[key])
#         return items[key]
#     else:
#         return None
    
    


# def get_description(key): 
#     items = {'F':'Unsatisfactorily', 
#            'FX':'Unsatisfactorily', 
#            'E':'Enough', 
#            'D':'Satisfactorily', 
#            'C':'Good', 
#            'B':'Very good', 
#            'A':'Perfectly'}
#     if key in ['F', 'FX', 'E', 'D', 'C', 'B', 'A']: 
#         print(items[key])
#         return items[key]
#     else:
#         return None
   

## Task 5

# def lookup_key(data, value):
#     data_new = []
#     for key, num in data.items():
#         if value == num:
#             data_new.append(key)
#         # else:
#         #     return 
#     print(data_new)
#     return data_new


## Task 6

# def split_list(grade):
#     under_avr = []
#     above_avr = []
#     try:
#         avr = sum(grade) / len(grade)
#         for i in grade:
#             if i <= avr:
#                 under_avr.append(i)
#             if i > avr:
#                 above_avr.append(i)
#         grade_new = (under_avr, above_avr)
#         return grade_new
#     except ZeroDivisionError:
#         return ([], [])

# def split_list(scores):
#     if not scores:  # Якщо список порожній, повертаємо два порожні списки
#         return [], []

#     average = sum(scores) / len(scores)  # Знаходимо середнє значення балів

#     lower_half = [score for score in scores if score <= average]
#     upper_half = [score for score in scores if score > average]

#     return lower_half, upper_half

# # Приклад використання функції
# scores = [85, 90, 78, 92, 88, 76, 95, 89]
# lower, upper = split_list(scores)
# print("Значення менше або рівні середньому:", lower)
# print("Значення більше середнього:", upper)


## Task 7

# points = {
#     (0, 1): 2,
#     (0, 2): 3.8,
#     (0, 3): 2.7,
#     (1, 2): 2.5,
#     (1, 3): 4.1,
#     (2, 3): 3.9,
# }


# def calculate_distance(coordinates):
#     if len(coordinates) <= 1:
#         return 0
    
#     total_distance = 0

#     for i in range(len(coordinates) - 1):
#         start, end = sorted((coordinates[i], coordinates[i + 1]))
#         distance = points.get((start, end), points.get((end, start), 0))
#         total_distance += distance
        
#     return total_distance
    


# def calculate_distance(coordinates, points):
#     if len(coordinates) <= 1:
#         return 0  # Повертаємо 0 для порожнього списку та списку з однією координатою

#     total_distance = 0

#     for i in range(len(coordinates) - 1):
#         # Сортуємо координати у кортежі так, щоб завжди менша була першою
#         start, end = sorted((coordinates[i], coordinates[i + 1]))
#         print(start, end)
        
#         # Отримуємо відстань між початковою і кінцевою точками зі словника
#         distance = points.get((start, end), points.get((end, start), 0))
#         print(distance)
        
#         total_distance += distance

#     return total_distance

# # Приклад використання функції
# points = {(0, 1): 2, (0, 2): 3.8, (0, 3): 2.7, (1, 2): 2.5, (1, 3): 4.1, (2, 3): 3.9}
# coordinates = [0, 1, 3, 2, 0]
# distance = calculate_distance(coordinates, points)
# print("Загальна відстань: ", distance)


## Task 8

        
# def game(terra, power):
#     final_power = power
#     for lst in terra:
#         for i in lst:
#             if final_power >= i:
#                 final_power += i       
#             else:
#                 break
#     print(final_power)
#     return final_power     

## Task 9

# def is_valid_pin_codes(pin_codes):
#     if len(pin_codes) == 0:
#         return False  
#     for pin in pin_codes:
#         if len(pin) == 4 and len(pin_codes) == len(set(pin_codes)):
#             if any(char.isalpha() for char in pin):
#                 print(False)
#                 return False
#             else:
#                 True
#         else:
#             print(False)
#             return False
#     if True:
#         print(True)
#         return True 
# is_valid_pin_codes(['1101', '9034', '0011'])
    
 

#  def is_valid_pin_codes(pin_codes):
#     # Перевірка на порожній список
#     if not pin_codes:
#         return False
    
#     # Створюємо множину для зберігання унікальних пін-кодів
#     unique_codes = set()

#     for code in pin_codes:
#         # Перевірка довжини пін-коду (4 символи)
#         if len(code) != 4:
#             return False
        
#         # Перевірка, чи всі символи - цифри
#         if not code.isdigit():
#             return False
        
#         # Додаємо пін-код до множини унікальних кодів
#         unique_codes.add(code)
    
# #     # Перевірка на наявність дублікатів
# #     if len(unique_codes) == len(pin_codes):
# #         return True
# #     else:
# #         return False


# ## Task 10 and 11

# from random import randint


# def get_random_password():

#     password = ('')
#     while len(password ) <= 7:
#         random_num = chr(randint(40, 126))
#         password += random_num
#     print(password)    
#     return password
    
    

# get_random_password()


## Task 11

# def is_valid_password(password):

#     if  len(password) == 8: #and any(char.isdigit() for char in password) and any(char.islower() for char in password) and any(char.isupper() for char in password):
#         print(True)
#     else:
#         print(False)

# is_valid_password('AAAa9')


## Tasl 12     Випадковий пароль


# from random import randint


# def get_random_password():
#     result = ""
#     count = 0
#     while count < 20:
#         random_symbol = chr(randint(40, 126))
#         result = result + random_symbol
#         count = count + 1
#     print(result)
#     return result


# def is_valid_password(password):
#     if len(password) != 20:
#         return False

#     has_upper = False
#     has_lower = False
#     has_num = False

#     for ch in password:
#         if ch.isupper():
#             has_upper = True
#         elif ch.islower():
#             has_lower = True
#         elif ch.isdigit():
#             has_num = True
#     return has_upper and has_lower and has_num


# def get_password():
    
#     valid = False

#     while valid == False:
#         password =  get_random_password()
#         valid = is_valid_password(password)
#         print(valid)
#     print(password)
#     return password   
    
# get_password()


## Task 13


from pathlib import Path


# p = Path('/Users/zhutk/OneDrive/Документы/Repository/Start')

# def parse_folder(path):
#     files = []
#     folders = []
#     p = Path(path)
    
#     for i in p.iterdir():
#         if i.is_file() == True:
#             files.append(i.name)
#         else:
#             folders.append(i.name)
#             print(i.name)


#     print (files, folders)        
#     return files, folders
 
# parse_folder('/Users/zhutk/OneDrive/Документы/Repository/Start')


## Task 14

# import sys


# def parse_args():
    
#     list_of_argv = []
#     result = ""
    
#     for i in sys.argv:
#         if i != sys.argv[0]:
#             list_of_argv.append(i)
         
#     result = ' '.join(list_of_argv)
#     print(result)
#     return result

# parse_args()



## Task 8  ХЗ як працює) в плані, без'i' не працює, ален й вона не працює

def game(terra, power):
    final_power = power
    for lst in terra:
        for i, val in enumerate(lst):
            print(val)
            if power >= val:
                final_power += val      
            else:
                break
    print(final_power)
    return final_power 

game([[1, 1, 5, 10], [10, 2], [1, 1, 1]], 1)



