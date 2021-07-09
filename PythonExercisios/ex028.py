import random
import time
lista = [0,  1, 2, 3, 4, 5]
a = random.choice(lista)
nome = str(input('Olá! Eu sou o Clarke.\nQual o seu nome?\n')).strip().title()
if nome == 'Donovan':
    print('Que nome lindo você tem!! :-D')
    print(f'É um prazer te conhecer, {nome}!  :-)')
else:
    print('Você tem um nome tão normal!')
    print(f'É um prazer te conhecer {nome}')
print(f"""{nome} eu acabei de pensar em um número entre 0 e 5.
Será q vc consegue adivinhar qual é?""")
j = int(input('Digite o um número entre 0 e 5:\n'))
print('PROCESSANDO...')
time.sleep(2)
if j == a:
    print(f'Parabéns, {nome}!!!\nVocê acertou. O Número que eu pensei foi {a}')
else:
    print(f"""Que pena, {nome}. Não foi dessa vez.
O número que eu pensei foi {a}.
Você errou. 
''\(º_º)/''""")
