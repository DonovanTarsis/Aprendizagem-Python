cc = str(input('Em que cidade você nasceu? ')).title().strip().split()
c = cc[0]
s = 'Santo' in c[:5]
print(f'O primeiro nome da sua cidade é "Santo"? {s}')
