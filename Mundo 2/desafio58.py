'''Melhora o jogo do
DESAFIO 028 onde o
computador vai
"pensar" em um
número entre 0 a 10. Só
que agora o jogador vai
tentar adivinhar até
acertar. mostrando no
final quantos palpitas
Foram necessários
para vencer.'''

from random import randint
from time import sleep
cores = {
    'vermelho':'\033[4;31m',
    'limpa':'\033[m'
}

numero = randint(0, 10)
palp = 1
print('-=-' * 30)
print('Vou pensar em um numero de 0 a 10. Tente adividinhar...')
print('-=-' * 30)
digitado = int(input('Digite um numero: '))

print('{}PROCESSANDO...{}'.format(cores['vermelho'], cores['limpa']))
sleep(2)

while digitado != numero:
    print('Você Errou, te darei mais uma chance!')
    digitado = int(input('Digite outro numero: '))
    palp += 1

print("VOCÊ ACERTOU O NUMERO É {}".format(numero))
print('Só precisou de {} tentativa(s)!'.format(palp))
