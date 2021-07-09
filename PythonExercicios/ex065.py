parar = False
c = me = ma = t = 0
while not parar:
    c += 1
    n = int(input('Digite um número:'))
    t += n
    if c == 1:
        me = ma = n
    if n > ma:
        ma = n
    if n < me:
        me = n
    o = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if o == 'N':
        parar = True
m = t / c
print(f"""Você informou {c} valores.
O maior valor digitado foi: {ma}
O menor valor digitado foi: {me}
A média entre todos os valores é: {m}""")
