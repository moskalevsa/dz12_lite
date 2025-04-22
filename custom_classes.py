"""
Cкрипт, который собирает информацию обо всех файлах в директории `data/processed/`
 и сериализует их в JSON-файл.
"""
import json
import os
import time
from pprint import pprint

from dzlog import write_log


class FileInfo:
    """
    Класс содержащий информацию о файле
    """

    def __init__(self, filename: str, filePath: str, filesize: int, lastmod: str):
        self.filename = filename
        self.filePath = filePath
        self.filesize = filesize
        self.lastmod = lastmod

    def get_print_str(self):
        """
        получить f строку для печати
        """
        output1 = f'мя файла : {self.filename}.\n Полный путь к файлу : {self.filePath}. \n '
        output2 = f'Размер файла : {self.filesize}.\n ата создания и последнего изменения файла : {self.lastmod}.\n'
        output = output1 + output2
        return output

    def __str__(self):
        return self.get_print_str()


class File_info_list:
    """
     Класс содержащий список информации о файлах
    """

    def __init__(self, f_info_list: list[:FileInfo]):
        self.f_info_list = f_info_list

    def __str__(self):
        output = f'Список информациио  файлах:\n'
        for file in self.f_info_list:
            output = output + file.get_print_str()
        return output

    def get_file_info_list(self):
        return self.f_info_list


def file_to_dict(file: FileInfo):
    """
    перевод в словарь класса информция о файле
    """
    dict = {}
    dict.update({"1. file name": file.filename})
    dict.update({"2. full file path": file.filePath})
    dict.update({"3. file size": file.filesize})
    dict.update({"5. last change": file.lastmod})
    return dict


def fileifolist_to_dict(fileinfo_list: File_info_list):
    """
    Перевод в словарь класса список информации о файлах
    """
    list_dict = []
    result_dict = {}
    file_list = fileinfo_list.get_file_info_list()
    for i in range(len(file_list)):
        dict = file_to_dict(file_list[i])
        list_dict.append(dict)
    result_dict.update({"Список файлов": list_dict})
    return result_dict


# Определение текущей директории
maindir = os.getcwd()
# print (f'текущая директория: {maindir}')
# Смена текущей директории
os.chdir('poject_root')
project_dir = os.getcwd()
print(f'текущая директория: {project_dir} ')

# Смена текщей дрректории . на data/processed
# print(os.getcwd())
os.chdir('data/processed')
print(f'текущая директория: {os.getcwd()}')

# Получение списка имен oбработанных файлов
file_read = os.listdir(os.getcwd())
print(f'Список имен файлов заполнен:\n {file_read} ')

# Получение списка путей oбработанных файлов
file_list_path = []  # Список размеров файлов в байтах
for i in range(len(file_read)):
    flr = file_read[i]
    pth = 'proiect_root/data/processed/' + flr
    file_list_path.append(pth)
print(f'Список путей файлов заполнен:\n {file_list_path} ')

# Получение списка размеров файлов в байтах
file_list_size = []  # Список размеров файлов в байтах
for i in range(len(file_read)):
    flr = file_read[i]
    fsize = os.path.getsize(flr)
    file_list_size.append(fsize)
print(f'Список размеров файлов заполнен:\n {file_list_size} ')

# Получение даты последних изменеий файлов
file_list_last = []  # Список размеров файлов в байтах
for i in range(len(file_read)):
    flr = file_read[i]
    md_time = os.path.getmtime(flr)
    rd_time = time.ctime(md_time)
    file_list_last.append(rd_time)
print(f'Список последних изменеий файлов заполнен:\n {file_list_last} ')

# Получить список объектов информация о файлел
list_failinfo = []
for i in range(len(file_read)):
    fileinfo = FileInfo(file_read[i]
                        , file_list_path[i]
                        , file_list_size[i]
                        , file_list_last[i]
                        )
    list_failinfo.append(fileinfo)

# Создание объекта список файлов
infofile_list = File_info_list(list_failinfo)
# преобразование объекта в словарь
dictfileinfolist = fileifolist_to_dict(infofile_list)
print(f'Результат перевода объекта infofile_list в словарь -----')
pprint(dictfileinfolist)

# Смена текщей дрректории . на output/
os.chdir(project_dir)
# print (os.getcwd())
os.chdir('output')
# print (f'смена текущей директории на: {os.getcwd()}')

# помещение в json файл - сериализация
filew = 'file_info.json'
with open(filew, 'w', encoding='utf-8') as file:
    json.dump(dictfileinfolist, file)

# загрузка из  json файла - десериализация
with open(filew, 'r', encoding='utf-8') as file:
    loaded_data = json.load(file)

print(f'Результат десериализации joson -----')
pprint(loaded_data)

# Смена текущей директории
os.chdir(project_dir)
filelog = 'logs/dz_log.log'
# print (f'смена текущей директории на: {os.getcwd()}\n')
# Журналирование
message = (f'Список имен файлов заполнен\n')
write_log(filelog, message)

message = f'Список путей файлов заполнен:\n'
write_log(filelog, message)

message = f'Список размеров файлов в байтах составлен\n'
write_log(filelog, message)

message = f'Список дат последнего изменеия файлов заполнен\n'
write_log(filelog, message)

message = f'Oбъект - Cписок объектов данные файла заполнен\n'
write_log(filelog, message)

message = f'проведена сериализация в файл {filew}\n'
write_log(filelog, message)

message = f'проведена десериализация из файла {filew}\n'
write_log(filelog, message)
