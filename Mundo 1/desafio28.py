from random import randint
from time import sleep
cores = {
    'vermelho':'\033[4;31m',
    'limpa':'\033[m'
}
numero = randint(0, 5)
print('-=-' * 30)
print('Vou pensar em um numero de 0 a 5. Tente adividinhar...')
print('-=-' * 30)
digitado = int(input('Digite um numero: '))

print('{}PROCESSANDO...{}'.format(cores['vermelho'], cores['limpa']))
sleep(2)
if(digitado == numero):
    print("VOCÊ ACERTOU O NUMERO É {}".format(numero))
else:
    print('Você errou, o numero era {}{}{}'.format(cores['vermelho'], numero, cores['limpa']))