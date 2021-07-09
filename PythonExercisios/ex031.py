d = int(input('Qual a distância que irá viajar?\nDigite a distância em km:'))
if d <= 200:
    v = d * 0.50
else:
    v = d * 0.45
print(f'O valor da sua passagem é de R${v:.2f}')
