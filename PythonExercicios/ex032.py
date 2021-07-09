import datetime
a = int(input('Que ano quer analisar?\nColoque 0 para analisar o ano atual:'))
if a == 0:
    a = datetime.date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'Sim, o ano {a} é Bissexto.')
else:
    print(f'Não, o ano {a} não é Bissexto.')
