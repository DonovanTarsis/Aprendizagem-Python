n = int(input('Digite um número inteiro e descubra se ele é primo:'))
s = 0
if n == 2:
    s = 2
elif n != 2 and n > 2 and n % 2 == 1:
    for c in range(1, n + 1):
        a = n % c
        if a == 0:
            s += 1
if s == 2:
    print(f'{n} é um número primo.')
else:
    print(f'{n} não é um número primo.')
