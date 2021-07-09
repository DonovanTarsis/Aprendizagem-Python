n = str(input('Digite um frase sem acentos: ')).upper().strip()
nb = n.split()
na = ''.join(nb)
i = len(na)
s = []
# s = na [::-1]
for c in range(i-1, -1, -1):
    s += [na[c:c+1]]
s = ''.join(s).strip()
print(f'{na} invertido fica: {s}.')
if na == s:
    print(f'A frase: "{n}", é um palíndromo.')
else:
    print(f'A frase "{n}", não é um palíndromo.')
