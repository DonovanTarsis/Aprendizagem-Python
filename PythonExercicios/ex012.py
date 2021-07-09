pi = float(input('Digite o preço atual:R$'))
d = float(input('Digite a % de desconto:'))
vd = (pi/100)*d
pf = pi-vd
print('Valor: R${0:.2f}\nDesconto de {1:.0f}%: R${2:.2f}\nValor com desconto: R${3:.2f}'.format(pi, d, vd, pf))
