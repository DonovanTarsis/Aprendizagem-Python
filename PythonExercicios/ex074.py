from random import randint
menor = maior = 0
n1 = n2 = n3 = n4 = n5 = 0
for c in range(1, 6):
    s = randint(0, 9)
    if c == 1:
        n1 = s
        maior = menor = s
    elif c == 2:
        n2 = s
    elif c == 3:
        n3 = s
    elif c == 4:
        n4 = s
    elif c == 5:
        n5 = s
    if s > maior:
        maior = s
    elif s < menor:
        menor = s

nuns = (n1, n2, n3, n4, n5)
print(f'Os números sorteados foram: {nuns}')
print(f'O menor número foi {menor}')
print(f'O maior número foi {maior}')