'''Faça um programa que leia um número inteiro a diga se ela é ou não um número primo.'''
n1 = int(input('Digite um numero: '))
tot = 0
for c in range(1, n1 + 1):
    if(n1 % c == 0):
        print('\033[31m{} \033[m'.format(c), end='')  
        tot += 1 
    else:
        print('\033[33m{} \033[m'.format(c), end='')
if tot == 2:
    print('\n{} é primo!'.format(n1))
else:
    print('\n{} não é primo! porque tem {} divisores'.format(n1, tot))
