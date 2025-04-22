"""
Создание и запись данных в файлы d lbhtrnjhb. кфц
"""
import os

from dzfilework import write_file
from dzlog import write_log

# Определение текущей директории
maindir = os.getcwd()
print(f'текущая директория: {maindir}')

# Смена текущей директории
os.chdir('poject_root')
print(f'смена текущей директории на: {os.getcwd()}')

# Начало записи файлов
filelog = 'logs/dz_log.log'
message = (f'Начало записи файлов в директорию {os.path.join('project_root/data/raw')}\n')
# print(message)
write_log(filelog, message)

# Запись файлов в директорию raw
# Смена текущей директории
os.chdir('data/raw')
print(f'смена текущей директории на: {os.getcwd()}')

# Запись файла архитектурный подход(начало)
text = ['В общем и целом архитектурный подход основывается на выявлении и формулировании\n',
        'архитектуры деятельности предприятия, которая определяет архитектуру информационных систем\n',
        'а та, в свою очередь, определяет технологическую архитектуру.\n',
        'На каждом из этих трех уровней выделяются аспекты:\n',
        'архитектуры данных, архитектуры информационной безопасности, архитектуры интеграции и взаимодействия,\n',
        'а также архитектуры результативности и эффективности.']

namefile = 'architectura_approach.txt'
messagearh = write_file(namefile, text)

# Запись части документации Cisco Unified Contact Center Express Design Guide,
text = ['Advanced IVR Ports HTTP Triggers the web analog to Unified CM Telephony',
        'to invoke and run a workflow. HTTP triggers enable\n',
        'a Unified CCX to receive a customer\n',
        'contact request through an HTTPrequest.\n',
        'This approach allows web users to be offered service through a “click to talk to an agent” button.\n',
        'Information collected using the web\n',
        'a customer call back number, account number,shopping cart content,\n',
        'and so on) can be passed to the Unified CCX script to allow\n',
        'customer profile-based routing and a data-rich window.\n',
        'These contacts can be prioritized and routed using the same methods\n',
        'available to normal inbound voice callers.']
namefile = 'CiscoDesignGuide.txt'
messagecisco = write_file(namefile, text)

# Запись файла приход мамы)
text = ['Мама приходит в дом,\n',
        '- С ужасом глядя кругом...\n',
        '- С нами случился налёт?\n',
        '- Демон пришёл Бормоглот?\n',
        '- С орками эльфы сошлись?\n',
        '- Небо обрушилось вниз?\n',
        '- Жуткий прошёл ураган?\n',
        '- Или взорвался вулкан?\n',
        '- Может, "резвился" дракон?\n',
        '- Стая влетела горгон?\n',
        '- Полный "подкрался песец"?\n',
        '- Белому Свету конец?!\n',
        '- Не-е-е... Просто приходил дружок,\n',
        '- Поиграли мы "чуток".\n',
        '- Как прекрасно... Оказалось,\n',
        '  Я напрасно волновалась.']

namefile = 'mother_parish.txt'
messagemth = write_file(namefile, text)

# Смена текущей директории
os.chdir(maindir)
os.chdir('poject_root')
print(f'смена текущей директории на: {os.getcwd()}')
filelog = 'logs/dz_log.log'

# Начало внесение результатов записи в жкрнал
write_log(filelog, messagearh)
write_log(filelog, messagemth)
write_log(filelog, messagecisco)

# окончание записи файлов
message = (f'Окончание записи файлов в директорию {os.path.join('project_root/data/raw')}\n')
write_log(filelog, message)
