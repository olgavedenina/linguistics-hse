import re

with open('mystem.xml', encoding = 'utf-8') as f:
    text = f.read()

se = re.findall(r'<w>.*</w>',text)

count = len(se)

new_file = input('Введите имя файла, в который будет записана информация:   ')

with open(new_file, 'w', encoding = 'utf-8') as f:
    f.write(str(count))

print('Информация записана. Спаисбо, что воспользовались программой!')
    
