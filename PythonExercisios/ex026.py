f = str(input('Digite uma frase:\n')).strip().upper()
a = f.count('A')
pa = f.find('A') + 1
ua = f.rfind('A') + 1
print(f"""A letra "A" aparece {a} vezes na frase.
A primeira letra "A" apareceu na posição {pa}.
A última letra "A" apareceu na posição {ua}""")
