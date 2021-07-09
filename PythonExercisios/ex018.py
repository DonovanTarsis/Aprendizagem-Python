from math import sin, cos, tan, radians
a = float(input('Digite o ângulo:'))
r = radians(a)
print(' O sen de {0}° é:{1:.2f}\n O Cos de {0}° é:{2:.2f}\n A Tan de {0}° é:{3:.2f}'.format(a, sin(r), cos(r), tan(r)))
