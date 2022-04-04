''' Fasa um programa que mostra na tala uma contagam regressiva para o estouro da Fogos de artifício. 
indo de 10 até 0. com uma pausa de 1 segundo antra alas.'''
from time import sleep

cores = {
    'verde':'\033[4;32m',
    'vermelho':'\033[4;31m',
    'limpa':'\033[m'
}

for c in range(10, -1, -1):
    print('{}{:2}{}'.format(cores['vermelho'], c, cores['limpa']))
    sleep(1)

print('{}FOGOS{}'.format(cores['verde'], cores['limpa']))
