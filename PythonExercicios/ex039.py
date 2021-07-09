from datetime import date
a = int(input('Digite o ano em que nasceu:'))
i = date.today().year - a
if i < 18 and 18 - i != 1:
    print(f"""Ainda não chegou a hora de alistar-se.
Ainda faltam {18 - i} anos, até o seu alistamento.""")
elif i < 18 and 18 - i == 1:
    print(f"""Ainda não chegou a hora de alistar-se.
Mas, se prepare. Seu alistamento deve ser feito no próximo ano!""")
elif i == 18:
    print("""É hora de se alistar.
Você que completa 18 anos deve se alistar este ano!""")
elif i > 18 and i - 18 != 1:
    print(f"""Já passou a época do seu alistamento.
Seu alistamento ocorreu a {i - 18} anos.""")
elif i > 18 and i - 18 == 1:
    print(f"""Já passou a época do seu alistamento.
Seu alistamento ocorrreu há {i - 18} ano.""")
