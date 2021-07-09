mp = 0
nm = ""
mnp = 0
nmp = ""
for c in range(0, 5):
    n = str(input('Digite seu nome:')).title()
    p = float(input('Digite o seu peso:'))
    if c == 0:
        mp = p
        nm = n
        mnp = p
        nmp = n
    elif p > mp:
        mp = p
        nm = n
    elif p < mnp:
        mnp = p
        nmp = n
print(f"""O maior peso lido foi o de {nm}, que pesa {mp:.2f}KG.
O menor peso lido foi o de {nmp}, que pesa {mnp:.2f}KG.""")
