"""
Функция помещения сообщения в лог
"""
import datetime


def write_log(logfile, message: str):
    """
    запись сообщения в журнал с указанием времени
    """
    with open(logfile, 'a', encoding='utf-8') as file:
        logmessage = f'{datetime.datetime.now().strftime("%d.%m.%Y, %H:%M")} INFO: {message}'
        file.write(logmessage)
    return
