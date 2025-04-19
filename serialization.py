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
            получить f строку для печати
            """
            output1 = f'file name : {self.filename}\n original text : {self.text_isx} \n text : {self.text_proc}\n '
            output2 =f'byte size : {self.filesize}\n last change : {self.lastmod}\n'
            output = output1 + output2
            return output

    def __str__(self):
         return self.get_print_str()

class File_data_list:
    """
     Класс содержащий список данных файлов
    """
    def __init__(self, f_data_list : list[:File_data]):
        self.f_data_list = f_data_list
    def __str__(self):
        output = f'Список данных файлов:\n'
        for file in self.f_data_list:
            output = output + file.get_print_str()
        return output
    def get_file_data_list(self):
        return self.f_data_list


def file_to_dict (file : File_data):
    """
    перевод в словарь данных файла
    """
    dict = {}
    dict.update({ "1. file name" : file.filename })
    dict.update({ "2. original text" : file.text_isx })
    dict.update({ "3. text" : file.text_proc })
    dict.update({"4. file size" : file.filesize })
    dict.update({"5. last change": file.lastmod})
    return dict

def filedatalist_to_dict (filedata_list :File_data_list):
    """
    Перевод в словарь списка данных файла
    """
    list_dict = []
    result_dict = {}
    file_list = filedata_list.get_file_data_list()
    for i in range(len(file_list)):
        dict = file_to_dict(file_list[i])
        list_dict.append(dict)
    result_dict.update({"Список файлов" : list_dict})
    return    result_dict

# Определение текущей директории
maindir = os.getcwd()
print (f'текущая директория: {maindir}')

#Смена текущей директории
os.chdir('poject_root')
print (f'смена текущей директории на: {os.getcwd()} ')

# Получение списка исъодных текстов
#Смена текущей директории
os.chdir('data/raw')
print (f'смена текущей директории на: {os.getcwd()} для чтения исходных файлв')

#Смена текущей директории
os.chdir( maindir)
os.chdir('poject_root')
filelog = 'logs/dz_log.log'
print (f'смена текущей директории на: {os.getcwd()}\n')

#чтение файлов в директорию raw
#Смена текущей директории
os.chdir('data/raw')
print (f'смена текущей директории на: {os.getcwd()}')

file_list_r = os.listdir(os.getcwd())
print(f'Список файлов заполнен:\n {file_list_r}')

#Чтение исходных файлов
text_read =[] #Список прочитанных текстов
message_log1 = [] #Список сообщений о прочтнении файла для журналирования
for i in range(len(file_list_r)):
    flr  = file_list_r[i]
    encflr = determ_encoding(flr)  # Определение кодировки
    textf = read_file(flr, encr = encflr)
    text_read.append(textf)
    messagef = f'INFO: файл {flr} прочитан\n'
    message_log1.append(messagef)

# Смена текщей дрректории . на data/processed
os.chdir( maindir)
os.chdir('poject_root')
print(os.getcwd())
os.chdir('data/processed')
print (f'смена текущей директории на: {os.getcwd()}')

#Получение списка имен oбработанных файлов
file_read_proc = os.listdir(os.getcwd())
print(f'Список обработанных файлов заполнен:\n {file_read_proc} для чтения преобразованных файлов')

#Получение списка обработанных текстов
text_read_proc =[] #Список прочитанных исходных текстов
message_log2 = [] #Список сообщений о прочтнении файла для журналирования
for i in range(len(file_read_proc)):
    flr  = file_read_proc[i]
    encflr = determ_encoding(flr)  # Определение кодировки
    textf = read_file(flr,  encflr)
    text_read_proc.append(textf)
    messagef = f'INFO: файл {flr} прочитан\n'
    message_log2.append(messagef)

#Получение списка размеров файлов в байтах
file_list_size = []   #Список размеров файлов в байтах
for i in range(len(file_read_proc)):
    flr  = file_read_proc[i]
    fsize = os.path.getsize(flr)
    file_list_size.append(fsize)

#Получение даты последнего изменеия файла
file_list_last = []   #Список размеров файлов в байтах
for i in range(len(file_read_proc)):
    flr  = file_read_proc[i]
    md_time = os.path.getmtime(flr)
    rd_time = time.ctime(md_time)
    print(f"Last modified: {rd_time}")
    file_list_last.append(rd_time)

# Получить объект список файлоа
list_faildata = []
for i in range(len(file_read_proc)):
    filedata = File_data ( file_list_r[i]
                       ,text_read[i]
                       ,text_read_proc[i]
                       ,file_list_size[i]
                       ,file_list_last[i]
                       )
    list_faildata.append(filedata)

datafile_list = File_data_list(list_faildata)

# проверка преобразования класса в словарь
dictlist = filedatalist_to_dict(datafile_list)
print(f'Результат перевода объекта datafile_list в словарь -----')
pprint(dictlist)

#Смена текщей дрректории . на # Смена текщей дрректории . на output/
#Смена текущей директории
os.chdir( maindir)
os.chdir('poject_root')
os.chdir('output')
print (f'смена текущей директории на: {os.getcwd()}')

filew = 'processed_data.json'
with open(filew, 'w', encoding = 'utf-8') as file:
    json.dump(dictlist, file)
with open(filew, 'r', encoding = 'utf-8') as file:
    loaded_data = json.load(file )

print (print(f'Результат десериализации joson -----'))
pprint(loaded_data)

#Смена текущей директории
os.chdir( maindir)
os.chdir('poject_root')
filelog = 'logs/dz_log.log'
print (f'смена текущей директории на: {os.getcwd()}\n')

for i in range(len(message_log1)):
    message = message_log1[i]
    write_log(filelog, message)

for i in range(len(message_log2)):
    message = message_log2[i]
    write_log(filelog, message)

message = (f'Списки  текстов составлены\n')
write_log(filelog, message)

message = f'Список размеров файлов в байтах составлен\n'
write_log(filelog, message)

message = f'Список дат последнего изменеия файлов заполнен\n'
write_log(filelog, message)

message = f'Oбъект - Cписок объектов данные файла сохдан\n'
write_log(filelog, message)


message = f'проведена сериализация в файл {filew}\n'
write_log(filelog, message)
message = f'проведена десериализация из файла {filew}\n'
write_log(filelog, message)
