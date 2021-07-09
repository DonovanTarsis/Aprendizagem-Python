m = h = mn = c = 0
while True:
    i = int(input('Qual sua idade?'))
    s = ' '
    while s not in 'MF':
        s = str(input('Qual seu sexo?[M/F]')).strip().upper()[0]
    if i >= 18:
        m += 1
    if s == 'M':
        h += 1
    if s == 'F' and i < 20:
        mn += 1
    c += 1
    o = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
    while o not in 'SN':
        o = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
    if o == 'N':
        break
print(f'{c} pessoas se cadastraram.\n{m} pessoas com mais de 18 anos.\n{h} homens.\n{mn} mulheres com menos de 20 anos')
