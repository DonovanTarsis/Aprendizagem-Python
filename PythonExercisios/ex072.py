numeros = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', \
          'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte'
while True:
    n = int(input('Digite um número entre 0 e 20:'))
    while not 0 <= n <= 20:
        n = int(input('Tente novamente.\n Digite um número entre 0 e 20:'))
    print(f'Voce digitou o número {numeros[n]}.')
    while True:
        o = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if o in 'SN':
            break
    if o in 'N':
        break
print('FIM')
