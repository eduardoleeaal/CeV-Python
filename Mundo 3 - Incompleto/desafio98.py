'''Faça um programa
que tenha uma Função
chamada contador().
que receba três
parâmatros: inicio, Fim
e passo e realize a
contagam.

Seu programa tem que
realizar três
contagens através da
função criada:

a) Da 1 até 10, de 1 em 1
b) Da 10 até 0, de 2 em 2
c) Uma contagam personalizada.

https://prnt.sc/28ZXzWJydT-d
'''
from time import sleep
def contador(i, f, p):
    print('-=-' * 20)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até o {f} de {p} em {p}')
    sleep(2)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end = '', flush = True)
            sleep(0.25)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end = '', flush = True)
            sleep(0.25)
            cont -= p
        print('FIM!')
    

#Programa Principal
contador(0, 10, 1)
contador(10, 0, 2)

print('-=-' * 20)
print('Agora é sua vez de personalizar!')
inicio = int(input("INICIO: "))
fim = int(input("FIM: "))
passo = int(input("PASSO: "))
contador(inicio, fim, passo)