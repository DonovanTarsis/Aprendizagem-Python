c = t = 0
while True:
    n = int(input('Digite um valor qualquer, ou 999 para sair do programa:'))
    if n == 999:
        break
    t += n
    c += 1
print(f'Soma dos {c} valores digitados é {t}')
