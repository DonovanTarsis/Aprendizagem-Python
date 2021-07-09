"""n = int(input('Digite um número para\ncalcular seu fatorial:'))
resultado = False
a = 1
na = n
r = 0
while not resultado:
    if na == n:
        r = na * (na-a)
        na = na - a
    elif na < n and na > 1:
        r = r * (na-a)
        na = na - a
    elif na == 1:
        resultado = True
print(f'{n}! = {r}')"""
r = 1
n = int(input('Digite um número para\ncalcular seu fatorial:'))
for c in range(n, 1, -1):
    r = c * r
print(f'{n}! = {r}')
