print('imc')
peso = float(input('Digite o peso? (Kg): '))
altura = float(input('Digite a altura? (m): '))

imc = peso / (altura*altura)
limite = 25

if  limite >= imc:
    print('Acima do peso ideal')
else:
    print('Está no peso ideal')
