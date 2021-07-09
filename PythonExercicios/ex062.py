pt = int(input('Digite o primeiro termo da P.A.:'))
r = int(input('Digite a razão da P.A.:'))
c = 0
t = 10
parar = False
while not parar:
    print(pt)
    pt += r
    c += 1
    if c == t:
        x = int(input('Deseja mostrar mais quantos termos?'))
        if x == 0:
            parar = True
        else:
            t += x
print('Programa finalizado.')
