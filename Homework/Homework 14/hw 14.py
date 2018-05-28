text = input('Введите название файла: ')
with open(text, encoding = 'utf-8') as f:
    new_text = f.read()

punct = """.,?!-()/«»—:;"'"""
for i in punct:
    if i in new_text:
        new_text = new_text.replace(i, '')

word_len = [print('{}_{}'.format(word, len(word))) for word in new_text.split()]

    
