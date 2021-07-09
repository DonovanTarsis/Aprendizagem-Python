v = int(input('Digite sua velocidade em km\h:\n'))
m = (v - 80) * 7
if v > 80:
    print(f"""Você foi multado por excesso de velocidade.
A multa por excesso de velocidade é de R$7,00 para cada 
km excedido do limite de 80km/h.
Sendo assim, sua multa totaliza o valor de R${m:.2f}""")
print('Tenha um bom dia! Dirija com segurança!')
