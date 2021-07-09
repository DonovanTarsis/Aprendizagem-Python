s = float(input('Digite o salário atual: R$'))
pa = float(input('Digite a % de aumento:'))
a = s*((100+pa)/100)
print('Salário atual: R${0:.2f}\nPorcentagem de aumento:{1:.0f}%\nSalário atualizado: R${2:.2f}'.format(s, pa, a))
