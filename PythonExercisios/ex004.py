# a = input('Digite algo: ')
# print(f'O tipo primitivo desse valor é {type(a)}')
# print(f'Só tem espaços? {a.isspace()}')
# print(f'É um número? {a.isnumeric()}')
# print(f'É alfabético? {a.isalpha()}')
# print(f'É alfanumérico? {a.isalnum()}')
# print(f'Está em maiúsculas? {a.isupper()}')
# print(f'Está em minúsculas? {a.islower()}')
# print(f'Está capitalizado? {a.istitle()}')
n1 = input('Digite algo')
print(n1, type(n1))
print('{0} é numérico? {1}.'.format(n1, n1.isnumeric()))
print('É alfabético? {}.'.format(n1.isalpha()))
print('É ASCII? {}.'.format(n1.isascii()))
print('É Decimal? {}.'.format(n1.isdecimal()))
print('É um dígito? {}.'.format(n1.isdigit()))
print('É identificador? {}.'.format(n1.isidentifier()))
print('É mais baixo? {}.'.format(n1.islower()))
print('É imprimível? {}.'.format(n1.isprintable()))
print('É espaço? {}.'.format(n1.isspace()))
print('É título? {}.'.format(n1.istitle()))
print('É Caixa Alta? {}'.format(n1.isupper()))