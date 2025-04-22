"""
Чтение и обработка данных
- чтение всеx файлов из директории `data/raw/`, с определением их кодировок.
- преобразование данных из каждого файла, заменяя в них все заглавные буквы на строчные и наоборот.
- сохранение обработанных данныч в новые файлы в директорию `data/processed/`
  с сохранением исходных имен файлов, но добавив к ним суффикс `_processed`.
"""
import os

from dzfilework import determ_encoding
from dzfilework import read_file
from dzfilework import string_process
from dzfilework import write_file
from dzlog import write_log

# Определение текущей директории
maindir = os.getcwd()
print(f'текущая директория: {maindir}')

# Смена текущей директории
os.chdir('poject_root')
print(f'смена текущей директории на: {os.getcwd()}')

# Начало чтения файлов
filelog = 'logs/dz_log.log'
message = f'Начало чтения файлов из директории {os.path.join('project_root/data/raw')}\n'
write_log(filelog, message)

# чтение файлов в директорию raw
# Смена текущей директории
os.chdir('data/raw')
print(f'смена текущей директории на: {os.getcwd()}')

file_read_dir = os.getcwd()
file_list_r = []
for fl in os.listdir(file_read_dir):
    file_list_r.append(fl)
print(f'Список файлов заполнен:\n {file_list_r}')

# Чтение файлов
text_read = []  # Список прочитанных текстов
message_log = []  # Список сообщений о прочтнении файла для журналирования
for i in range(len(file_list_r)):
    flr = file_list_r[i]
    encflr = determ_encoding(flr)  # Определение кодировки
    textf = read_file(flr, encr=encflr)
    text_read.append(textf)
    messagef = message = f'INFO: файл {flr} прочитан\n'
    message_log.append(messagef)

# Внесение сообщений о прочтении в журнал
# Смена текущей директории
os.chdir(maindir)
os.chdir('poject_root')
print(f'смена текущей директории на: {os.getcwd()}')
# окончание записи файлов
message = f'Окончание чтения файлов из директорию {os.path.join('project_root/data/raw')}\n'
write_log(filelog, message)
for mesage in message_log:
    write_log(filelog, mesage)

# преобразование текстов
text_write = []  # Список преобрзованных текстов  для записи
for i in range(len(text_read)):
    textf = text_read[i]
    textp = []  # Преобразованный текст
    for strin in textf:
        strp = string_process(strin)
        textp.append(strp)
    text_write.append(textp)

# Запись преобрзованных текстов
# изметение имен файлов
file_list_w = []
for i in range(len(file_list_r)):
    filenamer = str(file_list_r[i])
    filenamew = filenamer[:-4] + '_processed.txt'
    file_list_w.append(filenamew)

# Начало записи файлов
message = f'Начало записи преобразованных файлов в директорию {os.path.join('project_root/data/processed')}\n'
write_log(filelog, message)
# Смена текщей дрректории . на data/processed
os.chdir('data/processed')
print(f'смена текущей директории на: {os.getcwd()}')

message_log_w = []  # Список сообщений о записи преобразованого  файла для журналирования
for i in range(len(file_list_w)):
    filename = file_list_w[i]
    text = text_write[i]
    mes = write_file(filename, text)
    message_log_w.append(mes)

# Внесение сообщений о преобразовании и записи в журнал
# Смена текущей директории
os.chdir(maindir)
os.chdir('poject_root')
print(f'смена текущей директории на: {os.getcwd()}')
# Преобразование текстов завершено
message = (f'Преобразование текстов  и имен файлов завершено\n')
write_log(filelog, message)
message = (f'Начало записи файлов в директорию {os.path.join('project_root/data/processed')} \n')
write_log(filelog, message)
for mesage in message_log_w:
    write_log(filelog, mesage)
# окончание записи файлов
message = f'Окончание записи файлов в директорию {os.path.join('project_root/data/processed')}\n'
write_log(filelog, message)
