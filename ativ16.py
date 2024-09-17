# Crie um programa que receba o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal (IMC). O programa deve classificar o IMC da pessoa de acordo com a tabela a seguir:
# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 ≤ IMC < 25
# Sobrepeso: 25 ≤ IMC < 30
# Obesidade: IMC ≥ 30

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)   # ou (altura * altura)

print('Com um peso de {} e uma altura de {} você tem um IMC de {:.2f}'.format(peso,altura,imc))

if imc < 18.5:
    print('Você está abaixo do peso !')

elif imc <= 25:
    print('Você está no peso ideal !')

elif imc <= 30:
    print('Você está com sobre peso !')

elif imc <= 40:
    print('Você esta com Obesidade !')

elif imc > 40:
    print('Procure um medico urgente!!! Você esta com Obesidade Morbida !')