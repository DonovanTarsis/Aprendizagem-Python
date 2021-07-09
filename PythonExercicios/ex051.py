p = int(input('Digite o primeiro valor da P.A.:'))
r = int(input('Digite a razão para a P.A.:'))
for c in range(p, ((r*10)+p), r):
    print(c)
