"""
Функция помещения сообщения в лог
"""
import os
from idlelib.iomenu import encoding
import datetime

def write_log(logfile, message : str):
    with open(logfile, 'a', encoding ='utf-8') as file:
        logmessage = f'{datetime.datetime.now().strftime("%d.%m.%Y, %H:%M")} INFO: {message}'
        file.write(logmessage)
    return