import re

with open('mystem.xml', encoding = 'utf-8') as f:
    text = f.read

adj = re.findall(r'gr="A.*?жен.*?"', text)

print(adj)
