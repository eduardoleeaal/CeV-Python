'''Fasa um programa
que tenha uma FunSão
chamada maior(), que
receba vários
parâmatros com
valoras inteiros.
Sau programa tam que
analisar todos os
valoras e dizer qual
dalas é o maior.
https://prnt.sc/kXkieHV1al0k
'''
from random import randint
from time import sleep

cores ={
    'limpa':'\033[m',
    'verde':'\033[4;33m'
}
def maior(* num):
    print('-=-' * 20)
    cont = maior = 0
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print('Foram informados {} valores'.format(cont))
    print('O maior valor informado foi {}{}{}'.format(cores['verde'], maior, cores['limpa']))


maior(6, 4, 3, 2, 1, 20, 15)
maior(9, 4, 2, 13, 97, 20)
maior(randint(0, 30), randint(0, 30), randint(0, 30), randint(0, 30))
maior()
print('-=-' * 20)










#def maior(valores):
#    print('-=-' * 20)
#    if len(valores) == 0:
#        valores.append(0)
#    print("Analisando os valores passados... ")
#    print("Dos numeros ", end = '')
#    for n in valores:
#        print(f'{n} ', end='', flush = True)
#        sleep(0.3)
#    print(f'Foram passados {len(valores)} valores', flush = True)  
#    sleep(0.5)
#    print(f'O maior valor da lista é: {max(valores)}', flush = True)
#    sleep(0.3)
#
#    
#    
#
#lista1 = [6, 4, 3, 2, 1, 20, 15]
#lista2 = [9, 4, 2, 13, 97, 20]
#lista3 = [randint(0, 30), randint(0, 30), randint(0, 30), randint(0, 30)]
#lista4 = []
#
#maior(lista1)
#maior(lista2)
#maior(lista3)
#maior(lista4)
#
#print('-=-' * 20)
#