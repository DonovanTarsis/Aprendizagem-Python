import random
a = input('1° Nome:')
b = input('2° Nome:')
c = input('3° Nome:')
d = input('4° Nome:')
e = f'{a} {b} {c} {d}' .split()
random.shuffle(e)
print('Ordem de apresentação:\n{0}.'.format(e))
