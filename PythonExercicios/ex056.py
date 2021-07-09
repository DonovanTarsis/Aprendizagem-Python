si = 0
nh = ''
ih = 0
mn = 0
for c in range(0, 4):
    print('-'*5, f'{c+1}ª PESSOA', '-'*5)
    n = str(input('Nome:')).title()
    i = int(input('Idade:'))
    s = str(input('Sexo [M/F]:')).upper()
    if s == 'M' and i > ih:
        nh = n
        ih = i
    elif s == 'F' and i <= 20:
        mn += 1
    si += i
mi = si/4
print(f'A média de idade é de {mi:.1f} anos.')
if ih > 0:
    print(f'O homem mais velho se chama {nh} e tem {ih} anos.')
elif ih == 0:
    print('Nenhum homem respondeu a pesquisa.')
print(f'{mn} mulheres com menos de 21 anos respondeu a pesquisa.')
