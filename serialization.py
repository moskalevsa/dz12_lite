"""
Cкрипт для сериализации содержимого всех файлов из директории `data/processed/` в один JSON-файл.
   - Включить в этот JSON-файл следующую информацию:
     - Имя файла.
     - Исходный текст.
     - Преобразованный текст.
     - Размер файла в байтах.
     - Дата последнего изменения файла.
   - Сохранить JSON-файл в директорию `output/` с именем `processed_data.json`.

"""
import json
import os
from idlelib.iomenu import encoding
import time
import ipykernel
from xml.etree.ElementTree import indent
from dzlog import  write_log
from dzfilework import write_file
from dzfilework import determ_encoding
from dzfilework import read_file
from dzfilework import read_file
from dzfilework import string_process
from dataclasses import dataclass, asdict

class Contentfile:
    """
    Класс содержащий содержимое  файла
    """
    def __init__(self, filename :str, text_isx : list[str], text_proc :list[str], filesize : int, lastmod :str ):
        self.filename = filename
        self.text_isx = text_isx
        self.text_proc = text_proc
        self.filesize = filesize
        self.lastmod = lastmod

    def __str__(self):
        return {'имя файла' : self.filename
                ,'исходный текст' : self.text_isx
                ,'текст' : self.text_proc
                ,'размер' : self.filesize
                ,'последнее изменение' : self.lastmod
                }


def file_to_dict (file : Contentfile):
    return { 'имя файла' : file.filename
            ,'исходный текст' : file.text_isx
            ,'текст' : file.text_proc
            ,'размер в байтах' : file.filesize
            ,'время последнего изменения': file.lastmod
            }

# Определение текущей директории
print (f'текущая директория: {os.getcwd()}')

#Смена текущей директории
os.chdir('poject_root')
print (f'смена текущей директории на: {os.getcwd()}')

# Получение списка исъодных текстов
#Смена текущей директории
os.chdir('data/raw')
print (f'смена текущей директории на: {os.getcwd()}')

file_read_dir = os.getcwd()
file_list_isx = []
for fl in os.listdir(file_read_dir):
    file_list_isx.append(fl)
print(f'Список исходных файлов заполнен:\n {file_list_isx}')

#Получение списка исходных текстов
text_read_isx =[] #Список прочитанных исходных текстов
for i in range(len(file_list_isx)):
    flr  = file_list_isx[i]
    encflr = determ_encoding(flr)  # Определение кодировки
    textf = read_file(flr, encr = encflr)
    text_read_isx.append(textf)

print (text_read_isx[0])

# Смена текщей дрректории . на data/processed
#Смена текущей директории
os.chdir('..')
os.chdir('..')
os.chdir('data/processed')
print (f'смена текущей директории на: {os.getcwd()}')

#Получение списка имен файлов
file_read_dir = os.getcwd()
file_list_proc = []
for fl in os.listdir(file_read_dir):
    file_list_proc.append(fl)
print(f'Список обработанных файлов заполнен:\n {file_list_proc}')

#Получение списка обработанных текстов
text_read_proc =[] #Список прочитанных исходных текстов
for i in range(len(file_list_proc)):
    flr  = file_list_proc[i]
    encflr = determ_encoding(flr)  # Определение кодировки
    textf = read_file(flr,  encflr)
    text_read_proc.append(textf)

print(text_read_proc[0])

#Получение списка размеров файлов в байтах
file_size = []   #Список размеров файлов в байтах
for i in range(len(file_list_proc)):
    flr  = file_list_proc[i]
    fsize = os.path.getsize(flr)
    file_size.append(fsize)
print(f'Список размеров файлов заполнен:\n {file_size}')

#Получение даты последнего изменеия файла
file_last = []   #Список размеров файлов в байтах
for i in range(len(file_list_proc)):
    flr  = file_list_proc[i]
    md_time = os.path.getmtime(flr)
    rd_time = time.ctime(md_time)
    print(f"Last modified: {rd_time}")
    file_last.append(rd_time)
print(f'Список дат последнего изменеия файлов заполнен:\n {file_last}')
contentfile1 = Contentfile (file_list_proc[0]
                                ,text_read_isx[0]
                                ,text_read_proc[0]
                                ,file_size[0]
                                ,file_last[0]
                                )

#print(file_to_dict(contentfile1))

json_string = json.dumps(file_to_dict(contentfile1), indent=4)

print(type(json_string))

#print(f'строка json {json_string} ')

json_string_text = json_string.decode(encoding= 'utf-8')
#print (encjs)
print(f'строка json {json_string_text} ')





