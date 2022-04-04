'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, Que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entra eles (desconsiderando o Flag).'''
soma = quant = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    soma += n
    quant += 1
    
print(f'A soma desses {quant} números é {soma}')