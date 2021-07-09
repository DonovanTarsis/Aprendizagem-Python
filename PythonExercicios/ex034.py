s = float(input('Digite o valor do seu salário atual:\nR$'))
if s > 1250:
    ns = s * 1.10
else:
    ns = s * 1.15
print(f'Seu novo salário é de R${ns:.2f}')
