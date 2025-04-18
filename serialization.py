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
from fileinput import filename
from idlelib.iomenu import encoding
import time
from pprint import pprint

import ipykernel
from xml.etree.ElementTree import indent
from dzlog import  write_log
from dzfilework import write_file
from dzfilework import determ_encoding
from dzfilework import read_file
from dzfilework import read_file
from dzfilework import string_process
from dataclasses import dataclass, asdict



class File_data:
    """
    Класс содержащий данные  файла
    """
    def __init__(self, filename :str, text_isx : list[str], text_proc :list[str], filesize : int, lastmod :str ):
        self.filename = filename
        self.text_isx = text_isx
        self.text_proc = text_proc
        self.filesize = filesize
        self.lastmod = lastmod

    def get_print_str(self):
            """
            получить f строку для печати    :return:
            """
            output1 = f'file name : {self.filename}\n original text : {self.text_isx} \n text : {self.text_proc}\n '
            output2 =f'byte size : {self.filesize}\n last change : {self.lastmod}\n'
            output = output1 + output2
            return output

    def __str__(self):
         return self.get_print_str()

class File_data_list:
    """
     Класс содержащий список данных классов
    """
    def __init__(self, f_data_list : list[:File_data]):
        self.f_data_list = f_data_list
    def __str__(self):
        output = f'Список данных файлов:\n'
        for file in self.f_data_list:
            output = output + file.get_print_str()
        return output
    def get_f_data_list(self):
        return self.f_data_list


def file_to_dict (file : File_data):
    """
    перевод в словарь данных файла
    """
    return { "file name" : file.filename
            ,"original text" : file.text_isx
            ,"text" : file.text_proc
            ,"last change" : file.filesize
            ,"last change": file.lastmod
            }

def filedatalist_to_dict (filedata_list :File_data_list):
    """
    Перевод в словарь списка данных файла
    """
    list_dict = [ ]
    file_list = filedata_list.get_f_data_list()
    for i in range(len(file_list)):
        dict = file_to_dict(file_list[i])
        list_dict.append(dict)
    return { "List of data files" :  listdict
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
text_list_read_isx =[] #Список прочитанных исходных текстов
for i in range(len(file_list_isx)):
    flr  = file_list_isx[i]
    encflr = determ_encoding(flr)  # Определение кодировки
    textf = read_file(flr, encr = encflr)
    text_list_read_isx.append(textf)

print (text_list_read_isx[0])

# Смена текщей дрректории . на data/processed
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
text_list_read_proc =[] #Список прочитанных исходных текстов
for i in range(len(file_list_proc)):
    flr  = file_list_proc[i]
    encflr = determ_encoding(flr)  # Определение кодировки
    textf = read_file(flr,  encflr)
    text_list_read_proc.append(textf)

print(text_list_read_proc[0])

#Получение списка размеров файлов в байтах
file_list_size = []   #Список размеров файлов в байтах
for i in range(len(file_list_proc)):
    flr  = file_list_proc[i]
    fsize = os.path.getsize(flr)
    file_list_size.append(fsize)
print(f'Список размеров файлов заполнен:\n {file_list_size}')

#Получение даты последнего изменеия файла
file_list_last = []   #Список размеров файлов в байтах
for i in range(len(file_list_proc)):
    flr  = file_list_proc[i]
    md_time = os.path.getmtime(flr)
    rd_time = time.ctime(md_time)
    print(f"Last modified: {rd_time}")
    file_list_last.append(rd_time)
print(f'Список дат последнего изменеия файлов заполнен:\n {file_list_last}')
os.chdir('..')
# Получить список файлоа
list_faildata = []
for i in range(len(file_list_proc)):
    filedata = File_data ( file_list_proc[i]
                       ,text_list_read_isx[i]
                       ,text_list_read_proc[i]
                        ,file_list_size[i]
                        ,file_list_last[i]
                       )
    list_faildata.append(filedata)

datafile_list = File_data_list(list_faildata)

print(datafile_list)
#json_string = json.dumps(file_to_dict(file1), indent= 4)

#print(json_string)

#Смена текщей дрректории . на # Смена текщей дрректории . на output/
#os.chdir('..')
print (f'смена текущей директории на: {os.getcwd()}')
#os.chdir('output/')
#print (f'смена текущей директории на: {os.getcwd()}')

#filew = repr('test.json')
#print(filew)

#with open(filew, 'w', encoding = 'utf-8') as file:
#    file.write(json_string)

#with open(filew, 'r', encoding = 'utf-8') as file:
#    loaded_data = json.load(file )

#print (type(loaded_data))

#pprint(loaded_data)



