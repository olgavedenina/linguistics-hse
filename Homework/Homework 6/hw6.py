import random


def noun():
    with open('noun.txt', encoding='utf-8') as f:        
        noun = f.readlines()   
    return random.choice(noun)

def adj(noun):
    with open('adj.txt', encoding='utf-8') as f:
        adj = f.readlines()
    res = random.choice(adj) + ' ' + noun
    return res

def verb(subj, obj):
    
    with open('verb.txt', encoding='utf-8') as f:
        verb = f.readlines()
    res = subj + ' '  + random.choice(verb) + ' ' + obj
    return res


def verb_imper(obj):
    with open('verb_imper.txt', encoding='utf-8') as f:
        verb_imper = f.readlines
        res = random.choice(verb_imper()) + ' ' + obj
    return res

def verb_neg(subj, obj):
    with open('verb.txt', encoding='utf-8') as f:
        verb_neg = f.readlines
        res = subj + ' ' + 'не' + ' ' + random.choice(verb_neg()) + ' ' + obj
    return res

def verb_quest(subj, obj):
    with open('verb.txt', encoding='utf-8') as f:
        verb_quest = f.readlines
        res = random.choice(verb_quest()) + ' ' + 'ли' + ' ' + subj + ' ' + obj
    return res

def verb_if(subj, obj):
    with open('verb.txt', encoding='utf-8') as f:        
        verb_if = f.readlines
        res = subj + ' ' + random.choice(verb_if()) + ' ' + 'бы' + ' ' + obj
    return res
        

def sent_pos():
    res = verb(adj(noun()), adj(noun())) + '.'
    return res

def sent_neg():
    res = verb_neg(adj(noun()), adj(noun())) + '.'
    return res

def sent_quest():
    res = verb_quest(adj(noun()), adj(noun())) + '?'
    return res

def sent_imper():
    res = verb_imper(adj(noun())) + '!'
    return res

def sent_if():
    res = verb_if(adj(noun()), adj(noun())) + '.'
    return res


def rand_sent():
    a = random.choice([1,2,3,4,5])
    if a == 1:
        return sent_pos()
    if a == 2:
        return sent_neg()
    if a == 3:
        return sent_quest()
    if a == 4:
        return sent_imper()
    if a == 5:
        return sent_if()


for i in range(5):
    sent = rand_sent()
    sent = sent.capitalize()
    sent = sent.replace('\n', '')
    print(sent, end=' ')
    
    
    
    





