# https://prnt.sc/26ox02i

altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em Kg: '))

imc = peso / altura ** 2.0


if(imc < 18.5):
    situacao = 'Abaixo do peso'
elif(imc >= 18.5 and imc < 25):
    situacao = 'Peso ideal'
elif(imc >= 25 and imc < 30):
    situacao = 'Sobrepeso'
elif(imc >= 30 and imc < 40):
    situacao = 'Obesidade'
else:
    situacao = 'Obesidade mórbida'

print('Seu IMC é: {:.2f} \nSua situação: {}'.format(imc, situacao))