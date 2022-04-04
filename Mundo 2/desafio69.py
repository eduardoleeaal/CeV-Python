'''Crie um programa qua leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada. 
O programa daverá perguntar se o usuário quer ou não continuar. 
No final. mostre:
A) quantas pessoas tem mais da 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos da 20 anos.'''
from time import sleep
m18 = home = mulh = 0

while True:
    print('---' * 14)
    print('\tCadastre uma pessoa!')
    print('---' * 14)
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Digite seu sexo: '))
    if(idade > 18):
        m18 += 1
    if(sexo in 'Mm'):
        home += 1
    if(idade < 20 and sexo in 'Ff'):
        mulh += 1

    print('Deseja Continuar?')
    pergunta = str(input('--> ')).strip().upper()[0]
    while pergunta not in 'SsYyNn':
        print('Deseja Continuar?')
        pergunta = str(input('--> ')).strip().upper()[0]
    if pergunta not in 'SsYy':
        print('Encerrando!')
        sleep(1)
        break
print('-=-' * 20)
print('Quantidade de maiores de 18: {}'.format(m18))
print(f'Quantidade de homens cadastrados: {home}')
print('Quantidade de mulheres com menos de 20 anos: %d' %(mulh))
    