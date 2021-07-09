from random import choice
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
computador = choice(lista)
# print(computador)
print('Olá, sou seu computador.\nAcabei de pensar em um número entre 0 e 10.\n Será que você consegue adivinhar?')
jogador = int(input('Digite um número entre 1 e 10:'))
t = 1
while jogador != computador:
    jogador = int(input('Digite um número entre 1 e 10:'))
    t += 1
if t == 1:
    print('Parabéns!!!\nVocê acertou de primeira.')
else:
    print(f'Você acertou, mas precisou de {t} tentativas.')
