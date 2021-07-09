a = float(input('Digite a medida da Reta 1:'))
b = float(input('Digite a medida da reta 2:'))
c = float(input('Digite a medida da reta 3:'))
# if a + b > c:
#    if a + c > b:
#       if b + c > a:
#            print(f'Sim! As medidas {a}, {b} e {c} podem formar um triângulo.')
#        else:
#            print(f'Não. As medidas {a}, {b}, {c} não podem formar um triângulo.')
#    else:
#        print(f'Não. As medidas {a}, {b}, {c} não podem formar um triângulo.')
#else:
#    print(f'Não. As medidas {a}, {b}, {c} não podem formar um triângulo.')
if a + b > c and a + c > b and b + c > a:
    print(f'Os segmentos {a}, {b}, {c} PODEM formar um triângulo!')
else:
    print(f'Os segmentos {a}, {b}, {c} NÃO PODEM formar um triângulo!')
