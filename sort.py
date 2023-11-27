
import re
import sys
import os
import shutil
import fnmatch
from pathlib import Path, WindowsPath

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}



for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()
    
IMAGES_FORMATS = ["jpeg", "png", "jpg", "svg"] 
VIDEO_FORMATS = ["avi", "mp4", "mov", "mkv"] 
DOCS_FORMATS = ["doc", "docx", "txt", "pdf", "xlsx", "pptx", "xls"] 
MUSIC_FORMATS = ["mp3", "ogg", "wav", "amr"] 
ARCHIV_FORMATS = ["zip", "gz", "tar"] 
    
    
images = []
video = []
docs = []
music = []
archiv =[]
unknown_files = []
list_of_known_formats = set()
list_of_unknown_formats = set()


def normalize(name):        ## Функція для перейменування файлів
    translated_name = ''
    for i in name:
        if i.isalpha():
            translated_name += i.translate(TRANS)

        elif i.isdigit() or i == '.':
            translated_name += i 
        else:
            translated_name += '_'

    return translated_name

    
p = Path('/Users/zhutk/OneDrive/Рабочий стол/Мотлах')

## Функція перевіряє кожен файл, залежно від формату перекудує у відповідний список
## Якщо зустрічає папку, перезапускає себе (крім папок для сортування файлів)
## Окремо додає формат (suffix) до списку відомих чи не відомих форматів 
    
def check_file_formats(path):

    try:
        for i in path.iterdir():
            
            if i.is_file() == True:

                # Використовуємо fnmatch для фільтрації файлів за форматами зображень
                if any(fnmatch.fnmatch(i, f"*.{format}") for format in IMAGES_FORMATS):
                    images.append(i)
                    list_of_known_formats.add(i.suffix)
                # Використовуємо fnmatch для фільтрації файлів за форматами відео
                if any(fnmatch.fnmatch(i, f"*.{format}") for format in VIDEO_FORMATS):
                    video.append(i)
                    list_of_known_formats.add(i.suffix)
                # Використовуємо fnmatch для фільтрації файлів за форматами документів
                if any(fnmatch.fnmatch(i, f"*.{format}") for format in DOCS_FORMATS):
                    docs.append(i)
                    list_of_known_formats.add(i.suffix)
                # Використовуємо fnmatch для фільтрації файлів за форматами музики
                if any(fnmatch.fnmatch(i, f"*.{format}") for format in MUSIC_FORMATS):
                    music.append(i)
                    list_of_known_formats.add(i.suffix)
                # Використовуємо fnmatch для фільтрації файлів за форматами архівів
                if any(fnmatch.fnmatch(i, f"*.{format}") for format in ARCHIV_FORMATS):
                    archiv.append(i)
                    list_of_known_formats.add(i.suffix)
                # Варіант для невідомих форматів
                if i.suffix not in list_of_known_formats:
                    print(i)
                    list_of_unknown_formats.add(i.suffix)
            else:
                if i.name in ['images', 'video', 'documents', 'audio', 'archives']:
                    continue
                else:    
                    check_file_formats(i)

    except Exception as e:
        print(f"Помилка: {e}")
        
test = [WindowsPath('/Users/zhutk/OneDrive/Рабочий стол/Мотлах/20231014T170551Z-001.zip')]        

# Функція  приймає шлях та назву для нової папки, створює таку папку і переміщує файли в ту папку
def handling_to_group(path, new_folder_name):     
    
    new_folder_path = os.path.join(p, new_folder_name)
    os.makedirs(new_folder_path, exist_ok=True)
    
    try:
        for file in path:
            shutil.move(file, new_folder_path)
            
    except Exception as e:
        print(f"Помилка: {e}")
        
        
 
def extracting_archives(list_of_archives):
    
    if len(list_of_archives) >= 1:                          # Створення папки "archives", при умові, що архіви знайдені
        main_folder_path = os.path.join(p, 'archives')
        os.makedirs(main_folder_path, exist_ok=True)
        
    for archive in list_of_archives:
        
        archive_name = os.path.splitext(os.path.basename(archive))[0] ## Розділяє ім'я від розширення в кінці

        new_folder_path = os.path.join(main_folder_path, archive_name)  ## Створення підпапки з назвою архіва
        os.makedirs(new_folder_path, exist_ok=True)
        
        shutil.unpack_archive(archive, new_folder_path)   

        
        
    

    
 
       
# handling_to_group(test, 'images')
    



# check_file_formats(p)







