'''Cria um programa
qua tenha uma tupla
com várias palavras
(não usar acentos).
Depois disso. você
deve mostrar para
cada palavra. quais
SÃO as suas vogais.'''

palavras = ('TESTANDO',
            'CONTINUO',
            'EDUARDO',
            'CURSO',
            'COUNTERSTRIKE',
            'VALORANT')
for p in palavras:
    print(f'\nNa palavra {p} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
print('\n')
print('-=-' * 20)