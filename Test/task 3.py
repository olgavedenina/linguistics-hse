import re

with open('mystem.xml', encoding = 'utf-8') as f:
    text = f.read()

f_adj = re.findall(r'gr="A=.*?жен.*?" />(.*)</w>', text)

print(f_adj)

adj_edit = ', '.join(f_adj)

new_file = input('Введите имя файла, в который будет сохранена информация:   ')

with open(new_file, 'w', encoding = 'utf-8') as f:
    f.write(adj_edit)
  
print('Информация записана. Спасибо, что воспользовались программой!')
