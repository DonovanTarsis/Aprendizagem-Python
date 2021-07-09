import random
a = str(input('Adicione o 1° nome:'))
b = str(input('Adicione o 2° nome:'))
c = str(input('Adicione o 3° nome:'))
d = str(input('Adicione o 4° nome:'))
print('Participantes:\n{0};\n{1};\n{2};\n{3};\nO escolhido é: {4}'.format(a, b, c, d, random.choice([a, b, c, d])))
