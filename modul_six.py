# fh = open('test.txt', 'w+')
# fh.write('hello!')

# position = fh.tell()
# print(position) # 6

# fh.seek(2)
# position = fh.tell()
# print(position) # 1

# fh.read(3)
# position = fh.tell()
# print(position) # 3

# fh.close()




##  Task 1

import re
from pathlib import Path


# def total_salary(path):
    
#     ## file_path = Path(path) Думав, треба через pathlib працювати, але це виявилось необов'язково
#     sum = 0
#     file = open(path, 'r')  #напряму вказав адресу і норм, нічого зайвого не потібно
#     content = file.read()
#     salary = re.findall(r'[\d]{1,}', content)
#     for i in salary:
#         i = float(i)
#         sum += i
#     print(sum)
    
#     file.close()
#     return sum
   
    
# total_salary('/Users/zhutk/OneDrive/Документы/Repository/Start/test.txt')



## Task 2

# def write_employees_to_file(employee_list, path):
    
#     file = open(path, 'w')
#     list_of_employees = []
#     for i in employee_list:
#         list_of_employees.extend(i)
#     print(list_of_employees)
#     for i in list_of_employees:
#         file.write(i + '\n')
    
#     file.close()
    
# write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']], '/Users/zhutk/OneDrive/Документы/Repository/Start/test.txt')

## Task 3

# def read_employees_from_file(path):
    
#     file = open(path, 'r')
#     list_of_employees = []
#     for i in file:
#         i = i.replace('\n', '')
#         list_of_employees.append(i)
    
#     file.close()
#     print(list_of_employees)
#     return list_of_employees
    

    
# read_employees_from_file('/Users/zhutk/OneDrive/Документы/Repository/Start/test.txt')


## Task 4

# def add_employee_to_file(record, path):
#     file = open(path, 'a')
#     # list_of_employees = []
#     # for i in employee_list:
#     #     list_of_employees.extend(i)
#     # print(list_of_employees)
#     try:
#         file.write(record + '\n')
        
#     finally:
#         if file:
#             file.close()
    
# add_employee_to_file(['Drake Mikelsson,19'], '/Users/zhutk/OneDrive/Документы/Repository/Start/test.txt')


## Task 5

# def get_cats_info(path):
    
#     contacts = []
#     with open(path, 'r') as fh:
#         content = fh.read()
#         list_of_cont = re.findall(r'[\w]{24},[\w]{1,},[\d]{1,2}', content)
#         for i in list_of_cont:
#             new_dict = {}
#             value_1, value_2, value_3 = re.split(',', i)
#             new_dict['id'] = value_1
#             new_dict['name'] = value_2
#             new_dict['age'] = value_3
#             contacts.append(new_dict)
#         print(contacts)
#         return contacts
            
            
## Task 6

# def get_recipe(path, search_id):
#     with open(path, 'r') as fh:
#         content = fh.read()
#         recipe_pattern = re.search(str(search_id) + r'[\w\ ,]{1,}', content)
#         if recipe_pattern == None:
#             return None
#         recipe = {}
#         change = recipe_pattern.group()
#         # print(change)
#         parts = re.findall(r'[\w\ ]{1,}', change)
#         # print(parts)
#         recipe['id'] = parts[0]
#         recipe['name'] = parts[1]
#         ingridient_list = []
#         for i in range(len(parts)):
#             if i != 0 and i !=1:
#                 ingridient_list.append(parts[i])
#         recipe['ingredients'] = ingridient_list
#         print(recipe)
#         return recipe
    
    
    
# def get_recipe(path, search_id):
#     import re

#     with open(path, 'r') as fh:
#         content = fh.read()
#         recipe_pattern = re.findall(str(search_id) + r'[\w\ ,]{1,}', content)
#         if recipe_pattern == None:
#             return None
#         recipe = {}
       
#         change = recipe_pattern[0]
#         parts = change.split(',')
#         recipe['id'] = parts[0]
#         recipe['name'] = parts[1]
#         ingridient_list = []
#         for i in range(len(parts)):
#             if i != 0 and i !=1:
#                 ingridient_list.append(parts[i])
#         recipe['ingredients'] = ingridient_list
#         print(recipe)
#         return recipe
    
    
    
# get_recipe('/Users/zhutk/OneDrive/Документы/Repository/Start/test.txt', "60b90c2e13067a15887e1ae3")

    
# def sanitize_file(source, output):
#     final_content = ''
#     with open(source, 'r') as reading:
#         content = reading.read()
#         print(content)
#         numless_content = re.findall(r'[\D]', content)
#         print(numless_content)
        
#         for i in numless_content:
#             final_content +=i
#         print(final_content)
#     with open(output, 'w') as writing:
#         writing.write(final_content)
            
    
    
    
# sanitize_file('/Users/zhutk/OneDrive/Документы/Repository/Start/source.txt', '/Users/zhutk/OneDrive/Документы/Repository/Start/output.txt')


## Task 8

# def save_applicant_data(source, output):
    
    # lines = []
    # for obj in source:
    #     lines.append([str(value) for value in obj.values()])
    #     print(lines)
    # with open(output, 'w') as file_studinfo:
    #     for line in lines:
    #         print(','.join(line) + '\n')
    #         file_studinfo.write(','.join(line) + '\n')
    
# def save_applicant_data(source, output):    
#     applicants = []
#     for i in source:
#         applicants.append([str(value) for value in i.values()])   ##Щось я це слабо зрозумів, як саме це працює
#     print(applicants)                                             ##ну і тут  str треба ставити, хз, нащо
    
#     with open(output, 'w') as writing: 
#         for line in applicants:
#             writing.write(','.join(line) + '\n')             ## саме через join, інакше не працює
#             print(writing)
                

  # print(dict_of_applicants)
    # with open(output, 'w') as writing:
    #     for val in dict_of_applicants.values():
    #         print(val)
            



                
                
##  Task 9

# def is_equal_string(utf8_string, utf16_string):


        
#     first_string = utf8_string.decode()
#     print(first_string)
#     second_string = utf16_string.decode('utf-16')
#     print(second_string)
    
#     if first_string == second_string:
#         print(True)
#         return True
#     else:
#         print(False)
#         return False
    
    
# is_equal_string(b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82!', b'\xff\xfe\x1f\x04@\x048\x042\x045\x04B\x04!\x00')


##  Task 10

# def save_credentials_users(path, users_info):
    

#     with open(path, 'wb') as users:
#         for key, value in users_info.items():
#             person = f"{key}:{value}\n".encode()
#             users.write(person)
            
    
    
    
# save_credentials_users('/Users/zhutk/OneDrive/Документы/Repository/Start/password.txt', {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'})
                
            
## Task 11

# def get_credentials_users(path):
#     with open(path, '+rb') as file:
#         text = file.read().decode()
#         result = re.findall(r'[\w\:]{1,}', text)
#         print(result)
#         return result
    
    
    
# get_credentials_users('/Users/zhutk/OneDrive/Документы/Repository/Start/password.txt')       

## Task 12


# import base64

# message = "Hello world!"
# message_bytes = message.encode("utf-8")
# print(message_bytes)
# base64_bytes = base64.b64encode(message_bytes)
# print(base64_bytes)
# base64_message = base64_bytes.decode("utf-8")

# print(base64_message)  # SGVsbG8gd29ybGQh

# import base64     


# def encode_data_to_base64(data):
  
#     encoded_users = []
#     for user in data:
#       user_bytes = user.encode("utf-8")
#       base64_bytes = base64.b64encode(user_bytes)
#       encoded_users.append(base64_bytes.decode("utf-8"))
#     print(encoded_users)
#     return encoded_users
  
# encode_data_to_base64(['andry:uyro18890D', 'steve:oppjM13LL9e'])


##  Task 13        Архіви

# import shutil


# def create_backup(path, file_name, employee_residence):
  
#   with open(path + '/' + file_name, '+bw') as file:
#     for key, value in employee_residence.items():
#       person = f"{key}:{value}\n".encode()
#       file.write(person)
#   archive_name = shutil.make_archive('backup_folder', 'zip', path)
#   print(archive_name)
#   return archive_name
      
# create_backup('/Users/zhutk/OneDrive/Документы/Repository/Start/', 'named_file.txt', {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'})
     

            
            
## Task 14     Архіви


import shutil


def unpack(archive_path, path_to_unpack):
  shutil.unpack_archive(archive_path, path_to_unpack)
  
  
  
unpack('/Users/zhutk/OneDrive/Документы/Repository/Start/backup_folder.zip', '/Users/zhutk/OneDrive/Документы/Repository/Start/')
  
