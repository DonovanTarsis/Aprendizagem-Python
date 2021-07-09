a = float(input('Qual sua altura? '))
p = float(input('Qual o seu peso?'))
imc = p / a**2
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}, você está abaixo do peso.')
elif imc >=18.5 and imc < 25:
    print(f'Seu IMC é {imc:.2f}, você está no peso ideal.')
elif imc >= 25 and imc <30:
    print(f'Seu IMC é {imc:.2f}, você está acima do peso.')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC é {imc:.2f}, você está obeso.')
elif imc >= 40:
    print(f'Seu IMC é {imc:.2f}, você está em obesidade mórbida.')
