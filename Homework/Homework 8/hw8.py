import random

def begin():
    return 'Привет! Давай сыграем в игру? Я загадаю слово, а ты должен будешь отгадать его. Все просто! Поехали!'
    
def d(words, hints):
    d = {}
    with open(words, encoding = 'utf-8') as f:
        text = f.read()
        words = text.split('\n')
    with open(hints, encoding = 'utf-8') as f:
        text = f.read()
        hints = text.split('\n')
    for word in words:
        for hint in hints:
            if word in hint:
                d[word] = hint           
    return d

def game(d): 
    word = random.choice(d[word])
    attempts = len(values[hint])
    counter = attempts
    while counter != 0:
        print(d[word] + '.........')
        guess = input()
        if guess == attempt:
            print('Поздравляю, Вы выиграли!')
            break
        elif counter != 1:
            counter -= 1
            print('Не угадали, попробуйте еще раз!')
        else:
            print('К сожалению, Вы проиграли. Но не отчаивайтесь, Вы можете попробовать еще раз!')
            break
        
def main():
    
    print(begin())
    print(game(d))

main()
        
    
