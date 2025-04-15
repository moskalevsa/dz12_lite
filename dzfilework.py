"""
Содержит функции записи, чтения и обработки файлов
"""
import os
import datetime
from dzlog import  write_log
import chardet

def write_file(filew, text : list, enc = 'utf-8', ):
    """
    запись списка строк  в текстовый файл
    """
    with open(filew, 'w', encoding = enc ) as file:
         file.writelines(text)
         message = f'INFO: файл {filew} записан\n'
    return message

def determ_encoding (checkfile):
    """
    определение кодировки файла
    :param checkfile  - файл
    :return: кодировку файла
    """
    with open(checkfile, 'rb') as file:
       text_fl = file.read()
    result = chardet.detect(text_fl)
    encfl = result['encoding']
    return encfl

def read_file(filin,  encr = 'utf-8', ):
    """
    чтение списка строк  из текстового файла
    """
    with open(filin, 'r', encoding = encr ) as file:
        textfl = file.readlines()
    return textfl

def string_process (inputstr:str) -> str:
    """
    преобразование данных из каждого файла, заменяя в них все заглавные буквы на строчные и наоборот.
    :param inputstr - входная строка:
    :return: преобразованная строка
    """
    outputstr = str('')
    istr = 0
    for char in inputstr:
        chstrin = str(char)
        if chstrin.isalpha() and chstrin.isupper():
            chstrout = chstrin.lower()
        elif chstrin.isalpha() and chstrin.islower():
            chstrout = chstrin.upper()
        else:
            chstrout = chstrin
        if istr == 0:
            outputstr = str(chstrout)
        else:
            outputstr =outputstr + chstrout
        istr +=1
    return outputstr

#strtestin = '- Или взорвался вулкан?\n'
#print(f'Входная строка {strtestin}')
#strtestout = string_process(strtestin)
#print(f'Выходная строка {strtestout}')









