nc = str(input('Digite seu nome completo:\n')).title().strip().split()
nn = len(nc)
pn = nc[0]
un = nc[nn-1]
print(f"""Muito prazer em te conhecer!
Seu primeiro nome é {pn}.
Seu último nome é {un}.""")
