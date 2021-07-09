o = 0
while o != 5:
    a = int(input('Primeiro valor:'))
    b = int(input('Segundo valor:'))
    o = 0
    while o != 4 and o != 5:
        print("""    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
        o = int(input('>>>>> Qual é a sua opção?'))
        if o == 1:
            print(f'{a} + {b} = {a + b}')
        if o == 2:
            print(f'{a} x {b} = {a*b}')
        if o == 3:
            if a > b:
                print(f'{a} é o maio número.')
            elif a < b:
                print(f'{b} é o maior número.')
            elif a == b:
                print('Não existe um valor maior.')
        if o not in [1, 2, 3, 4, 5]:
            print('Opção inválida. Tente novamente.')
        print('=-='*10)
print('Programa finalizado.')
