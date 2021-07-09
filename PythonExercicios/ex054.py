from datetime import date
y = (date.today().year)
ma = 0
me = 0
for c in range(0, 7):
    a = int(input('Digite seu ano de nascimento:'))
    i = y - a
    if i  >= 21:
        ma += 1
    else:
        me += 1
print(f'{me} pessoas ainda não atingiram a maior idade. \n{ma} pessoas já atingiram a maior idade.')
