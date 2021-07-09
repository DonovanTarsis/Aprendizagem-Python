n = int(input('Digite um número:'))
print("""Escolha uma base de conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal""")
c = int(input('Digite sua escolha:'))
if c == 1:
    print(f'A conversão de {n} para BINÁRIO é: {(bin(n)[2:])}')
elif c == 2:
    print(f'A conversão de {n} para OCTAL é: {(oct(n)[2:])}')
elif  c == 3:
    print(f'A conversão de {n} para Hexadecimal é: {(hex(n)[2:])}')
else:
    print('Opção inválida. Tente novamente.')