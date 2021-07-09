s = str(input('Informe seu sexo: [M/F]')).upper().strip()[0]
while s not in 'MF':
    print('Dados inválido. Tente novamente.')
    s = str(input('Informe seu sexo: [M/F]')).upper().strip()[0]
print(f'Sexo {s} registrado com sucesso.')
