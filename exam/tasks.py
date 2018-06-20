import os
import re
import collections

start_path = '.'

for root, dirs, files in os.walk(start_path):
    for f in files:
        if f.endswith('.html'):
            with open(f, encoding = 'utf-8') as f:
                text = f.read()
                clean = re.compile('<.*?>')
            clean_text = re.sub(clean, '', text)
            symbols = '`'
            if symbols in clean_text:
                text = clean_text.replace(symbols, '')
            with open('news.txt', 'a', encoding = 'cp1251') as f:
                f.write(text)

print('Файл news.txt создан!')

for root, dirs, files in os.walk(start_path):
    for f in files:
        if f.endswith('.html'):
            with open(f, encoding = 'utf-8') as f:
                text = f.read()
                proper = re.findall(r'lex="([А-Я].*?)"', text)
            counter = collections.Counter(proper)
            with open('proper_frequency.txt', 'a', encoding = 'utf-8') as f:
                for key in counter:
                    print(key, '\t', counter[key], '\n')
                    


            
                
        
    
