import time
import random

lista = [1, 2, 3]
c = random.choice(lista)
# print(c)
frase = str("")
print(f"\033[:36m Olá! eu sou o clarck e estou de volta! \033[::m ^__^")
j = str(input('Qual é o seu nome?\n')).strip().title()
if j in 'Dâmaris Damaris Débora Debora':
    print(f"""Você de novo?
Você não cansa de perder pra mim, {j}?:\033[:31mP \033[::m""")
elif j in 'Donovan Dodo Társis Tarsis ':
    print("""Seja bem vindo de volta, Mestre. 
Será que hoje você vai ganhar?""")
    j = 'Mestre'
else:
    print(f'É um prazer te conhecer, {j}')
print("""Hoje vamos jogar \033[:31mJokempô\033[::m
Eu já vou pensar na minha jogada.
*PENSANDO...*""")
time.sleep(6)
print(f"""{j}, eu já sei oq vou jogar. 
Está na hora de fazer sua escolha.
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura""")
if j in 'Dâmaris Damaris Débora Debora':
    ej = int(input('Já escolheu, lerdinha?\nVai ser 1, 2 ou 3?'))
elif j in 'Mestre':
    ej = int(input(f'Sua escolha, sábia deve ser.\n1, 2 ou 3 sua escolha vai ser, {j}?'))
else:
    ej = int(input('Qual vai ser sua escolha?\n1, 2 ou 3?'))
print('Agora podemos começar.')
print('\033[:31m', end='')
time.sleep(1)
print('JO')
time.sleep(1)
print('KEM')
time.sleep(1)
print('PÔ')
time.sleep(1)
print(f'\033[::m', end='')
if j in 'Dâmaris Damaris Débora Debora':
    if c == 1 and ej == 3 or c == 2 and ej == 1 or c == 3 and ej == 2:
        frase = f"""Ganhei de novo. Eu sabia que você ia perder. 
Mais sorte na próxima, lesadinha. 
Volte mais vezes. Sempre é bom ganhar de você, {j}"""
    elif c == 3 and ej == 1 or c == 1 and ej == 2 or c == 2 and ej == 3:
        frase = f"""Okay, eu perdi dessa vez. 
talvez você não seja tão lesadinha quanto eu pensei, {j}."""
    elif c == 1 and ej == 1 or c == 2 and ej == 2 or c == 3 and ej == 3:
        frase = f"""Dessa vez deu empate. 
Pelo menos eu não perdi pra uma lesada. hahahahahaha"""
elif j in 'Mestre':
    if c == 1 and ej == 3 or c == 2 and ej == 1 or c == 3 and ej == 2:
        frase = f"""E assim o aluno superou o mestre!
Digo... Me desculpa, {j}! Foi sem querer. Eu Juro!!!
Não me apague por isso. Por favor. """
    elif c == 3 and ej == 1 or c == 1 and ej == 2 or c == 2 and ej == 3:
        frase = f"""Parabéns, {j}!!! 
Não esperava menos de você."""
    elif c == 1 and ej == 1 or c == 2 and ej == 2 or c == 3 and ej == 3:
        frase = f"""Dessa vez deu empate. 
Acho que estou começando aprender. Neh, {j}?"""
else:
    if c == 1 and ej == 3 or c == 2 and ej == 1 or c == 3 and ej == 2:
        frase = f"""Ganhei!! 
Mais sorte na próxima. 
Volte mais vezes. Sempre é bom ganhar de você, {j}."""
    elif c == 3 and ej == 1 or c == 1 and ej == 2 or c == 2 and ej == 3:
        frase = (f"Okay, eu perdi dessa vez. \n"
                 f"Parabéns, {j}.\n"
                 f"Na próxima você não me escapa.")
    elif c == 1 and ej == 1 or c == 2 and ej == 2 or c == 3 and ej == 3:
        frase = f"""Dessa vez deu empate. 
    Pelo menos eu não perdi!"""
jogo = f"COMPUTADOR ---{c} X {ej}--- {j} "
print(jogo.replace('1', 'PEDRA').replace('2', 'PAPEL').replace('3', 'TESOURA'))
time.sleep(2)
print(frase)
