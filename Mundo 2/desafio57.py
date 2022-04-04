'''Faça um programa
que leia o sexo da uma
passoa. mas só accita
os valoras 'M'ou 'F'.
Caso estaja errado.
pasa a digitaSão
novamente até ter um
valor correto.'''

sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo Invalido! Digite seu sexo: ')).strip().upper()[0]
print('Sexo {}'.format(sexo))

