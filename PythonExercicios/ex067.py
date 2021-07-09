print('=§='*13)
while True:
    n = int(input('Digite um número para ver sua tábuada.'))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:^2} = {n * c}')
        c += 1
    print('=§='*13)
print('Fim do programa')
