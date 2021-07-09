from random import randint
print('-=-' * 9, '\nVamos jogar par ou ímpar.')
print('-=-' * 9)
c = 0
while True:
    jogador = int(input('Digite um número:'))
    pi = str(input('Par ou Ímpar?[P/I] ')).strip().upper()[0]
    while pi not in 'PI':
        print('Opção inválida. Tente novamente')
        pi = str(input('Par ou Ímpar?[P/I]')).strip().upper()[0]
    if pi == 'P':
        pi = 'PAR'
    else:
        pi = 'ÍMPAR'
    comp = randint(1, 10)
    soma = jogador + comp
    r = soma % 2
    if r == 0:
        g = 'PAR'
    else:
        g = 'ÍMPAR'
    if g == pi:
        print(f'Você jogou {jogador} e o computador jogou {comp}. Deu {g}.')
        print('Você venceu!\nVamos jogar novamente.')
        c += 1
    else:
        print(f'Você jogou {jogador} e o computador jogou {comp}. Deu {g}.')
        break
print(f'GAME OVER! Você venceu {c} vezes')
