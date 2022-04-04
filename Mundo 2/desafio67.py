'''Faça um programa que mostra a tabuada da vários números.
Um da cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''
count = 1
while True:
    n = int(input('Digite um numero para ver a tabuada: '))
    if n <= 0:
        break
    print('-=-' * 20)
    for count in range(1, 11):
        print(f'{n:2} x {count:2} = {n * count}')
    print('-=-' * 20)
print('FIM!')