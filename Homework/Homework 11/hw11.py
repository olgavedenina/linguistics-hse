import re

with open('Ling.html', encoding = 'utf-8') as f:
    text = f.read()

html = re.sub(r'([\W<>])+(язык)(а|у|ом|е|и|ов|ам|ами|ах)?([\W<>])+', r'\1шашлык\3\4', text)
html = re.sub(r'([\W<>])+(Язык)(а|у|ом|е|и|ов|ам|ами|ах)?([\W<>])+', r'\1Шашлык\3\4', text)

new_file = input('Введите имя файла, в котором Вы хотите сохранить информацию:  ')

with open(new_file, 'w', encoding = 'utf-8') as f:
    f.write(html)

print('Информация записана. Спасибо, что воспользовались программой!')

