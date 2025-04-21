"""
Скрипт для создание резервной копии в архиве
и для разархивирования и восстановления данных из созданного архива резервной копии.
"""
import os
import shutil
from zipfile import ZipFile
import datetime
from dzlog import  write_log


#смена директорий, формирование путей и имени zip файла
os.chdir('poject_root')
dirproject = os.getcwd()
print (f'смена текущей директории на: {dirproject}')
filelog = 'logs/dz_log.log'
"""
Создание архива директории data и директоию baclups
"""
dir_path = os.path.join('.', 'data') # директория которую следует поместить в архив
# print(dir_path)

date = datetime.datetime.now().strftime("%Y%m%d" ) # получение даты в требуемом формате

new_file_name = 'backup' + date  # формирование имени архива

dst_path = os.path.join( 'backups') # полдлучения пути для архива
print(dst_path)

zipname = f'{dst_path}/{new_file_name}' # куда поместить архив
print(zipname)
message = f'Определены аривируемая директория {dir_path} и архив {zipname}\n '
write_log(filelog, message)
# Создание архива
#shutil.make_archive(zipname, 'zip', dir_path)
message = f'создан архив {zipname}\n '
write_log(filelog, message)
"""
Востановление из архива в директорию data2
"""
archive = zipname + '.zip' # Имя архива
dir_extr = os.path.join('..', 'data2') #директория в которую извлекаются файлы

with  ZipFile(archive, 'r') as zip_file:
    zip_file.extractall(dir_extr)
message = f'архив {arhive} распакован в директорию {dir_extr}\n '
write_log(filelog, message)


