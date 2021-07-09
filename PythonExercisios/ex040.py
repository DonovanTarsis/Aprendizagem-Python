from math import  trunc
n1 = float(input('Digite sua nota do 1º semestre:'))
n2 = float(input('Digite sua nota do 2º semestre:'))
m = ((n1 + n2) / 2)
if m < 5:
    print(f"""Você foi reprovado.
Sua média foi {m:.1f}
Estude mais.""")
elif m >= 5 and m <= 6.94:
    print(f"""Você está de recuperação.
Sua média foi  {m:.1f}
Estude bastante para as provas de recuperação!""")
elif m > 6.94:
    print(f"""Parabéns!!! 
Sua média foi {m:.1f}
Você foi aprovado.""")