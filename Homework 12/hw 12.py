import os
import re

path = input('Введите путь:   ')

if os.path.exists(path):
    file_list = os.listdir(path)
    count = 0
    for f in file_list:
        if os.path.isdir(f):
            if re.findall(r'[А-Яа-я]', f):
                count += 1                
    print('Все папки и файлы: ', file_list)
    if count == 1:
        print('Найдена', count, 'папка, названная кириллицей.')
    elif count == 2 or count == 3 or count == 4:
        print('Найдено', count, 'папки, названных кириллицей.')
    else:
        print('Найдено', count, 'папок, названных кириллицей.') 
    
else:
    print(path, 'не существует. Пожалуйста, перезапустите программу и введите путь еще раз.')
