"""
Валидация JSON с использованием JSON Schema
"""
from  jsonschema import validate, ValidationError, exceptions


schema0 = {
             "filename": {"type": "string"},
             "filepath": {"type": "string"},
              "filesize": {"type": "integer","minimum": 100 },
              "lastmod" : {"type": "string"}
         }

fileinfo = {
               'file name': 'CiscoDesignGuide_processed.txt'
              ,'full file path': 'proiect_root/data/processed/CiscoDesignGuide_processed.txt'
               ,' file size': 638
               ,'last change': 'Tue Apr 22 12:02:30 2025'
             }

print("Проверка fileinfo  по схеме0")
try:
    validate(instance=fileinfo, schema=schema0)
    print("Результат проверки fileinfo по схеме0 -  валиден")
except ValidationError as e:
    print(f"Результат проверки fileinfo по схеме0 - Ошибка валидации: {e}")

schema1 = {

    "properties": {
        'file name': 'CiscoDesignGuide_processed.txt'
        ,'full file path': 'proiect_root/data/processed/CiscoDesignGuide_processed.txt'
        ,'last change': 'Tue Apr 22 12:02:30 2025'
    }
}



fileinfo1 = {'file name': 234
    ,'full file path': 'proiect_root/data/processed/CiscoDesignGuide_processed.txt'
    ,'last change': 'Tue Apr 22 12:02:30 2025'}


print("Проверка fileinfo1  по схеме1")
try:
    validate(instance=fileinfo1, schema=schema1)
    print("Результат проверки fileinfo1 по схеме1 -  валиден")
except exceptions.SchemaError:
    print(f"Результат проверки fileinfo1 по схеме1 - Ошибка валидации")




