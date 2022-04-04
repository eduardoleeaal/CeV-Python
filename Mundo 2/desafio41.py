idade = int(input('Digite sua idade: '))

if idade <= 9:
    print('Nadador MIRIM')
elif idade <= 14 and idade > 9:
    print('Nadador INFANTIL')
elif idade <= 19 and idade > 14:
    print('Nadador Junior')
elif idade <= 20 and idade > 19:
    print('Nadador Sênior')
else:
    print('Nadador Master')