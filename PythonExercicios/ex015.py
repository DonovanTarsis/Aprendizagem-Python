d = int(input('Quantos dias de aluguel?:'))
km = float(input('Quantos km foram percorridos?:'))
va = (d * 60) + (km * 0.15)
print('O valor do aluguel é de R${0:.2f}'.format(va))
