p = float(input('Valor das compras: R$'))
print("""Método de pagamento:
[ 1 ] À vista no dinheiro/cheque: 10% de desconto.
[ 2 ] À vista no cartão: 5% de desconto.
[ 3 ] Em até 2x no cartão: S/ juros.
[ 4 ] 3x ou mais no cartão: 20% de juros.""")
mp =  int(input('Sua escolha: '))
if mp == 1:
    d = p * 0.1
    pf = p - d
    print(f"""Você escolheu pagar à vista no Dinheiro/cheque.
Você ganhou um desconro de 10 % no valor de:R${d:.2f}
O valor a ser pago é de: R${pf:.2f}""")
elif mp == 2:
    d = p * 0.05
    pf = p - d
    print(f"""Você escolheu pagar à vista no cartão.
Você ganhou um desconto de 5% no valor de: R${d:.2f}
O valor a ser pago é de: R${pf:.2f}""")
elif mp == 3:
    pf = p
    print(f"""Você escolheu pagar em até 2x no cartão.
O valor total a ser pago é de: R${pf:.2f}
Em 2x de R${pf/2:.2f}""")
elif mp == 4:
    j = p  * 0.2
    pf = p + j
    np = int(input('Vai parcelar em quantas vezes?'))
    print(f"""Você escolheu pagar em 3x ou mais no cartão.
Você pagará 20% de juros no valor de: R${j:.2f}
O valor total a ser pago é de: {pf:.2f}
Em {np}x de R${pf/np:.2f}""")
else:
    print('Opção inválida. Tente novamente.')
