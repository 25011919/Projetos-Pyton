# Descobrindo Imc 
peso = float(input('Peso (Kg): '))
altura = float(input('Altura (m): '))


imc = peso / (altura**2)

if  imc <= 44.7:
    situação = 'Peso mulheres'
elif imc >= 58:
    situação = 'Peso Homens'

print(f'Seu imc é = {imc:.2f}')