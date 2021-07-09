print('*'*23)
print('Sequência de Fibonacci.')
print('*'*23)
x = int(input('Quantos termos deseja mostrar?'))-1
na = 0
nb = 1
c = 0
print(f'{nb}→', end='')
while not c == x:
    c += 1
    t = na + nb
    print(f'{t}→', end='')
    na = nb
    nb = t
print('FIM')