"""
Функция помещения сообщения в лог
"""
import os
from idlelib.iomenu import encoding


def write_log(logfile :str, message : str):
    with open(logfile, message, 'a', encoding('utf-8')) as file:
        file.write(message)
    return