'''Cria um programa
qua vai gerar cinco
números alaatórios a
colocar am uma tupla.
Dapois disso. mostre a
listagam de números
gerados a também
Indique o manor co
maior valor que astão
na tupla.'''
from random import randint
numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(f'Valores sorteados:', end=' ')
for cont in numeros:
    print(cont, end=' ')
print('\nMaior: {}'.format(max(numeros)))
print('Menor: {}'.format(min(numeros)))
