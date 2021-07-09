from math import hypot, hypot
c1 = float(input('Valor cateto oposto:'))
c2 = float(input('Valor cateto adjacente:'))
# h = (c1**2 + c2**2)**(1/2)
print('A hipotenusa dos catetos {0} e {1} é igual a {2:.2f}'.format(c1, c2, hypot(c1, c2)))
