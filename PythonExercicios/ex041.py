from datetime import date
a = int(input('Digite o seu ano de nascimento:'))
i = date.today().year - a
if i <= 9:
    print('Você está na categoria Mirim.')
elif i > 9 and i <= 14:
    print('Vovê está na categoria Infantil.')
elif i > 14 and i <= 19:
    print('Você está na categoria Junior.')
elif i > 19 and i <= 25:
    print('Você está na categoria Sênior.')
elif i > 25:
    print('Você está na categoria Master.')
