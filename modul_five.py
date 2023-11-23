#   Task 1
# 
# 
# def real_len(text):
#     text_n = text.replace('\n', '')
#     text_t = text_n.replace('\t', '')
#     text_v = text_t.replace('\v', '')
#     text_r = text_v.replace('\r', '')
#     text_f = text_r.replace('\f', '')
#     real_len = len(text_f)
#     print(real_len)
#     return real_len

# def real_len(text):
#     result = 0
#     for e in text:
#         if e == '\n' or e == '\t' or e == '\v' or e == '\r' or e == '\f':
#             continue
#         result += 1
#     print(result)
#     return result

# real_len('Alex\nKdfe23\t\f\v.\r')



## Task 2     Складне)


# articles_dict = [
#     {
#         "title": "Endless ocean waters.",
#         "author": "Jhon Stark",
#         "year": 2019,
#     },
#     {
#         "title": "Oceans of other planets are full of silver",
#         "author": "Artur Clark",
#         "year": 2020,
#     },
#     {
#         "title": "An ocean that cannot be crossed.",
#         "author": "Silver Name",
#         "year": 2021,
#     },
#     {
#         "title": "The ocean that you love.",
#         "author": "Golden Gun",
#         "year": 2021,
#     },
# ]

# def find_articles(key, letter_case=False):
        
#     articles_result = []
#     key_lower = key.lower()
#     for article in articles_dict: #Окремо зробив цикл по словникам в списку
#         for i in article:    # І вже окремо оглядаю кожен словник
#             string = article.get(i)  # Використовуючи недооцінений метод get
            
#             if letter_case == True:
#                 if str(string).find(key) != -1:
#                  articles_result.append(article)
#             else:
#                 if str(string).find(key) != -1 or str(string).find(key_lower) != -1:
#                     articles_result.append(article)
                
    
#     print(articles_result)
#     return articles_result
        



##  Task 3 

# def sanitize_phone_number(phone):
    
#     clean_phone_number = ''
#     for i in phone:
#         if i != "+" and i != '-' and i != "(" and i != ")" and i != " ":
#             clean_phone_number += i
#     print(clean_phone_number)
#     return clean_phone_number


## Task 4

# def is_check_name(fullname, first_name):
#     check_name = fullname.removeprefix(first_name)
#     if check_name != fullname:
#         print(True)
#         return True
#     else:
#         print(False)
#         return False
    
    
# is_check_name('Max Old', 'Alex')


##  Task 5

# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone


# def get_phone_numbers_for_countries(list_phones):
    
#     test_get_phone_numbers_for_countries = {
#     "UA": [],
#     "JP": [],
#     "TW": [],
#     "SG": []
# }
 
#     for previous_number in list_phones:
#         number = sanitize_phone_number(previous_number)
#         if number.removeprefix('380') != number or number.removeprefix('0') != number:
#             test_get_phone_numbers_for_countries["UA"].append(number)   ##Тут цікавий момент, як 
#         elif number.removeprefix('81') != number:                       ##додати в список як значення за ключем
#             test_get_phone_numbers_for_countries["JP"].append(number)
#         elif number.removeprefix('886') != number:
#             test_get_phone_numbers_for_countries["TW"].append(number)
#         elif number.removeprefix('65') != number:
#             test_get_phone_numbers_for_countries["SG"].append(number)
#     print(f'{list_phones} == {test_get_phone_numbers_for_countries}')
#     return test_get_phone_numbers_for_countries

# get_phone_numbers_for_countries(['380998759405', '818765347', '8867658976', '657658976'])



##       Task 6

# def is_spam_words(text, spam_words, space_around=False):
    
    
#     for spam in spam_words:
#         spam_lower = spam.lower()
#         if text.find(spam) != -1:
#             # print(text.find(spam))
#             begin = text.find(spam)   #  початок спам-слова
#             print(begin)
#             end = text.find(spam) + len(spam) # кінець спамслова 
#             print(end)
#             if space_around == True:
#                 if (begin == 0 or text[begin - 1] == ' ') and (text[end] == '.' or text[end] == ' '):
#                     print(True)
#                     return True     
#                 else:
#                     print(False)
#                     return False
#             else:
#                 print(True)
#                 return True
#         elif text == -1:    
#             if text.find(spam_lower) != -1:
#                 begin = text.find(spam_lower)   #  початок спам-слова
#                 end = text.find(spam_lower) + len(spam_lower) # кінець спамслова 
#                 if space_around == True:
#                     if (begin == 0 or text[begin - 1] == ' ') and (text[end] == '.' or text[end] == ' '):
#                         print(True)
#                         return True
#                     else:
#                         print(False)
#                         return False
#                 else:
#                     print(True)
#                     return True
#         else:
#             print(False)
#             return False
            
                
# is_spam_words('The atmosphere at the match was terrifying.', ['match'], True)


## Task 7

# CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
# TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

# TRANS = {}

# for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
#     TRANS[ord(c)] = l
#     TRANS[ord(c.upper())] = l.upper()
    

# def translate(name):
#     translated_name = name.translate(TRANS)
#     print(translated_name)
#     return translated_name


## Task 8

# grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


# def formatted_grades(students):
    
#     students_grades = []
#     for keys in students:
#         student = '{:>4}|{:<10}|{:^5}|{:^5}'.format((len(students_grades) + 1), keys, students.get(keys), grades.get(students.get(keys)))
#         students_grades.append(student)
#     return students_grades
        
# for el in formatted_grades({"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}):
#     print(el)        

# formatted_grades({"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"})
        

## Task 9

        
# def formatted_numbers(number):
    
#     numbers = []
#     tital = '|{:^10}|{:^10}|{:^10}|'.format('decimal', 'hex', 'binary')
#     numbers.append(tital)
#     for i in range(number):
#         add_formatted_number = '|{:<10d}|{:^10x}|{:>10b}|'.format(i, i, i)
#         numbers.append(add_formatted_number)
#     return numbers


# for el in formatted_numbers(5):
#     print(el)


## Task 10        Регулярні вирази - норм тема

import re


# def find_word(text, word):
    
#     final_result = {
#     'result': None,
#     'first_index': None,
#     'last_index': None,
#     'search_string': word,
#     'string': text   
#     }
#     result = re.search(word, text)
#     if result:
#         final_result['result'] = True
#         start, end = result.span()
#         final_result['first_index'] = start
#         final_result['last_index'] = end
#     else:
#         final_result['result'] = False
#     print(final_result)
#     return final_result
        
    
# find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC \
# programming language, and first released it in 1991 as Python 0.9.0.","Python")


## Task 11


# import re


# def find_all_words(text, word):

#     pattern = re.compile(word, flags=re.IGNORECASE)   # Варіань один
#     result =  re.findall(pattern, text) 
#     ## result = re.findall(word, text, flags= re.IGNORECASE)    #Варіант два
#     print(result)
#     return result
     
# find_all_words("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC \
# programming language, and first released it in 1991 as python 0.9.0.","Python")


## Task 12

# import re


# def replace_spam_words(text, spam_words):

#     for word in spam_words:
#         text = re.sub(word, ('*' * len(word)), text, flags= re.IGNORECASE)
        
#     print(text)
#     return text
# # p = re.sub(r'(white)', 'color', 'blue socks and red shoes')
# # print(p)  # color socks and color shoes

# replace_spam_words('blue socks and red shoes', ['red', 'blue'])


## Task 13 

# import re


# def find_all_emails(text):
#     result = re.findall(r'[a-zA-Z]{1}[a-zA-Z0-9._]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,}', text)
#     print(result)
#     return result

# find_all_emails('Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net')


## Task 14 


# import re


# def find_all_phones(text):
#     result = re.findall(r"[+][3][8]0[(][\d]{2}[)][\d]{3}[-][\d]{1}[-][\d]{3}|[+][3][8]0[(][\d]{2}[)][\d]{3}[-][\d]{2}[-][\d]{2}", text)
#     print(result)
#     return result

# find_all_phones('Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787')



## Task 15

import re


# def find_all_links(text):
#     result = []
#     iterator = re.finditer(r"https?:\/\/[\w]{1,}.[\w]{2,}[\w\.]{1,}", text)
#     for match in iterator:
#         result.append(match.group())
#     return result

# def find_all_phones(text):
#     # result = re.findall(r"https:\/\/[\w]{1,}.[\w]{2,}[\w\.]{1,}|http:\/\/[\w]{1,}.[\w]{2,}[\w\.]{1,}", text)
#     result = re.findall(r"https?:\/\/[\w]{1,}.[\w]{2,}[\w\.]{1,}", text)
#     print(result)
#     return result

# find_all_phones('The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com ')

