import os
import zipfile
import shutil
import codecs
import re

# Функция распаковки архивов и удаления лишних файлов
def extract_and_delete(zip_file):
    # Распаковываем архив
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall()

    # Получаем список файлов в каталоге "1"
    dir_contents = os.listdir('1')

    # Находим файл, который начинается с "ON_NSCHFDOPPR"
    target_file = None
    for file in dir_contents:
        if file.startswith("ON_NSCHFDOPPR"):
            target_file = file
            break

    # Если найден файл, копируем его в текущий каталог и удаляем остальное
    if target_file:
        shutil.move(os.path.join('1', target_file), target_file)
        shutil.rmtree('1')  # Удаляем каталог "1"
        os.remove(zip_file)  # Удаляем zip-архив
        os.remove('meta.xml')  # Удаляем лишний файл
    else:
        print("Файл не найден в архиве", zip_file)
        
# Функция замены символов "_" на "-"
def replace_chars(text):
    return text.replace('_', '-')

# Получаем список всех файлов в текущем каталоге
files_in_current_directory = os.listdir()

# Фильтруем только zip-архивы
zip_files = [file for file in files_in_current_directory if file.endswith('.zip')]

# Применяем операции к каждому архиву
for zip_file in zip_files:
    extract_and_delete(zip_file)

# Каталог, в котором выполняется поиск xml файлов.
dir_path = os.getcwd()

# Шаблон для поиска файлов *.xml
pattern = re.compile('.*\.xml$')
# xml_files = [f for f in os.listdir('.') if f.endswith('.xml')]

# Поиск файлов *.xml и их обработка
for filename in os.listdir(dir_path):
    if pattern.match(filename):
        # Открываем файл в кодировке cp1251
        with codecs.open(filename, 'r', 'cp1251') as f:
            xml_content = f.read()
        
        # Заменяем символы "_" на "-"
        xml_content = re.sub(r'(ИдФайл|ИдОтпр|ИдПол)="([^"]*)"', lambda m: f'{m.group(1)}="{replace_chars(m.group(2))}"', xml_content)
        
        # Сохраняем изменения в файле
        with codecs.open(filename, 'w', 'cp1251') as f:
            f.write(xml_content)
