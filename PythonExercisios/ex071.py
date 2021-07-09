print('='*40)
nome = 'Banco DONOVAN'
print(f'{nome:^40}')
print('='*40)
while True:
    s = int(input('Qual o valor a ser sacado? R$'))
    if s >= 50:
        nc = s // 50
        s = s % 50
        print(f'{nc} Notas de R$50.00')
    if s >= 20:
        nv = s // 20
        s = s % 20
        print(f'{nv} Notas de R$20.00')
    if s >= 10:
        nd = s // 10
        s = s % 10
        print(f'{nd} Notas de R$10.00')
    if s >= 1:
        nu = s
        s = 0
        print(f'{nu} Notas de R$1.00')
    if s == 0:
        break
print('='*40)
fim = 'Obrigado por escolher o Banco DONOVAN'
print(f'{fim:^40}')
print('='*40)
