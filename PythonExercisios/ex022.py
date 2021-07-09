nc = str(input('Digite seu nome completo sem abreviação:')).strip()
nm = nc.upper()
nmi = nc.lower()
lista = nc.split()
nl = len(''.join(lista))
pn = lista[0]
nlpn = len(pn)
print('Analisando seu nome...')
print(f"""Seu nome em maiúsculas é {nm}.
Seu nome em minúsculas é {nmi}.
Seu nome tem ao todo {nl} letras.
Seu primeiro nome é {pn} e ele tem {nlpn} letras.""")
