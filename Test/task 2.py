import re
import collections

with open('mystem.xml', encoding = 'utf-8') as f:
    text = f.read()

morph = re.findall(r'gr="(.*)"', text)

word = {}
for key in morph:
    if key in word:
        value = word[key]
        word[key] = value + 1
    else:
        word[key] = 1

for key in word:
    print(key, '-', word[key], '\n')
    







