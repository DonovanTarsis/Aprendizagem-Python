print('=-='*10)
frase = 'Lojas Bicalho'
print(f'{frase:^30}')
print('=-='*10)
pb = c = t = pc = 0
npb = ''
while True:
    produto = str(input('Nome do produto:'))
    p = float(input('Preço: R$'))
    if c == 0 or p < pb:
        npb = produto
        pb = p
    if p >= 1000:
        pc += 1
    t += p
    c += 1
    o = '  '
    while o not in 'SN':
        o = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
    if o == 'N':
        break
print(f"""Total da compra: R${t:.2f}
Temos {pc} produtos que custam mais de R$1000.00
O produto mais barato foi {npb} que custa R${pb:.2f}""")
