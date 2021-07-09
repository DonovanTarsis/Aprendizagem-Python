nome = str(input('Qual o seu nome?\n').title().strip())
print(f"""Olá {nome}, eu irei analisar o empréstimo 
para sua casa nova.""")
vc = float(input('Qual o valor da casa que você pretende comprar?\nR$'))
sa = float(input('Qual o seu salário atual?\nR$'))
te = int(input('Em quantos anos você pretende pagar o empréstimo?\n'))
vp = vc / (te * 12)
if vp <= sa * 0.3:
    print(f"""Parabéns, {nome}!
O seu empréstimo foi aprovado.
Agora você está um passo mais perto de conseguir sua 
casa própia.
O seu empréstimo foi aprovado no valor de:
R${vc:.2f}
Você irá pagar {te * 12} parcelas no valor de:
R${vp:.2f}""")
else:
    print(f"""Sinto muito {nome}.
Seu empréstimo nao foi aprovado pois as parcelas 
excedem o limite de 30% do salário. """)
