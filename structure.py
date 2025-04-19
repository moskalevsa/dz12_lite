"""
Создание и управление директориями
"""
import os
import datetime
from contextlib import chdir

from dzlog import  write_log


def create_dir(dirname :str):
    isnew = True
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        isnew = True
    else:
        print(f'директория {dirname} уже существует')
        isnew = False
    return isnew

# Определение текущей директории
maindir = os.getcwd()
print (f'текущая директория: {maindir}')

# создание директории poject_root
isprojct_rootnew = create_dir('poject_root')

#Смена текущей директории
os.chdir('poject_root')
print (f'смена текущей директории на: {os.getcwd()}')

# Создание директории logs
islognew = create_dir('logs')

#Журналирование создания директорий project_root и logs
filelog = 'logs/dz_log.log'
if isprojct_rootnew:
    message = 'Создана директория project_root.\n'
    write_log(filelog,message)
if islognew:
   message = 'Создана директория logs.\n'
   write_log(filelog,message)
#Создание остальных директорий задания

# Создание директории data
isdatanew = create_dir('data')
if isdatanew:
    message = 'Создана директория data.\n'
    write_log(filelog,message)

#Смена текущей директории
os.chdir('data')
print (f'смена текущей директории на: {os.getcwd()}')

# Создание директории raw
israwnew = create_dir('raw')
# Создание директории processed
isprocessednew = create_dir('processed')

#Смена текущей директории
os.chdir( maindir)
os.chdir('poject_root')
print (f'смена текущей директории на: {os.getcwd()}')

#Журналирование создания директорий raw и processed
if israwnew:
    message = 'Создана директория raw.\n'
    write_log(filelog,message)
if isprocessednew:
    message = 'Создана директория processed.\n'
    write_log(filelog,message)

# Создание директории backups
isbackupsnew = create_dir('backups')
#Журналирование создания директориb backups
if isbackupsnew:
    message = 'Создана директория backups.\n'
    write_log(filelog,message)

# Создание директории output
isbackupsnew = create_dir('output')
#Журналирование создания директориboutput
if isbackupsnew:
    message = 'Создана директория output.\n'
    write_log(filelog,message)







