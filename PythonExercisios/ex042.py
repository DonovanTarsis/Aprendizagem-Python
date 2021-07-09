r1 = float(input('Digite o primeiro valor:\n'))
r2 = float(input('Digite o segundo valor:\n'))
r3 = float(input('Digite o terceiro valor:\n'))
if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    if r1 == r2 and r1 == r3:
        print('Esses três valores formam um triângulo Equilátero.')
    elif r1 == r2 and r1 != r3 and r2 != r3 or r1 != r2 and r1 == r3 and r2 != r3 or r1 != r2 and r1 != r3 and r2 == r3:
        print('Esses três valores formam um triângulo Isósceles.')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Esses três valores formam um triângulo Escaleno.')
else:
    print('Esses três valores não formam um triângulo.')
