time = 'Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', \
       'São Paulo', 'Internacional', 'Corinthians', \
       'Fortaleza Ec', 'Goiás', 'Bahia', 'Vasco da Gama', \
       'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', \
       'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí'
print('Brasileirão:')
print(time)
print('Os 5 primeiros colocados são:')
print(time[0:4])
print('Os últimos  são:')
print(time[16:])
print('Times em ordem alfabética:')
print(sorted(time))
print(f'A Chapecoense está na {time.index("Chapecoense") + 1}ª posição.')
print('O primeiro colocado é:')
print(time[0])
