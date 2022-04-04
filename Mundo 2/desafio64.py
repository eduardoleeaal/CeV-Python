'''Cria um programa
qua leia vários
números inteiros pelo
teclado. O programa só
vai parar quando o
usuário digitar o valor
999. No Final,
mostre quantos
números foram
digitados a qual foi a
soma entra alas
(desconsiderando o
flag).'''
cores = {
    'limpa':'\033[m',
    'vermelho':'\033[4;31m',
    'verde':'\033[4;32m'
}
n1 = 0
soma = 0
quant = 0
while n1 != 999:
    n1 = int(input('{}Para encerrar digite 999{} \nDigite um numero: '.format(cores['vermelho'], cores['limpa'])))
    if(n1 != 999):
        quant += 1
        soma += n1

print('A soma desses {}{}{} numeros é {}{}{} '.format(cores['verde'], quant, cores['limpa'], cores['verde'], soma, cores['limpa']), end='')