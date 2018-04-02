import re

text = input('Введите имя файла: ')

with open(text, encoding = 'utf-8') as f:
    html = f.read()

m = re.findall(r'lang="ru">(.*?)</h1>', html)
n = re.findall(r'<span class="no-wikidata".*title="\d* .*?">.*?(\d*).*?</a>', html)

uni = m [0]
year = n [0]

print('Найденная информация: ', uni, ' - ', year)

write = input('Введите имя файла, куда будет записана полученная инофрмация: ')

with open(write, 'a', encoding = 'utf-8') as f:
    f.write(uni)
    f.write(' - ')
    f.write(year)
    f.write(';\n')

print('Информация записана. Спасибо, что воспользовались программой!')
