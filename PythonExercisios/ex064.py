c = 0
t = 0
n = 0
while n != 999:
    n = int(input('Digite um valor qualquer, ou 999 para sair do programa:'))
    if n != 999:
        t += n
        c += 1
print(f'Soma dos {c} valores digitados é {t}')
