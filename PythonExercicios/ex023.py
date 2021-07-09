n = int(input('Digite um número inteiro de 0 - 9999:'))
lista = str((n / 1000))
# u = n // 1 % 10
# d = n // 10 % 10
# c = n // 100 % 10
# m = n // 1000 % 10
m = lista[0]
c = lista[2]
d = lista[3]
u = lista[4]
print(f"""Analisando o número {n} ...
Unidade: {u}
Dezena: {d}
Centena: {c}
Milhar: {m}""")
