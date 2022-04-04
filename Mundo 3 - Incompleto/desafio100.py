'''Fasa um programa
que tenha uma lista
chamada númaros a
duas FunSoas
chamadas sortaia() a
somaPar(). A primaira
funfão vai sortear 5
números e vai colocá-
los dentro da lista e a
sagunda funSão vai
mostrar a soma entra
todos os valoras
PARES sorteados pala
FunSão anterior.
https://prnt.sc/9yIWSOnlUFB6
'''
from random import randint
from time import sleep
numeros = list()
pares = list()


def sorteia(lista):
    print('Sorteando 5 valores para a lista: ', end = '')
    for i in range(0, 5):
        n = randint(0, 10)
        print(n, end=' ', flush = True)
        sleep(0.4)
        lista.append(n)
        
    print('PRONTO!')
    
def somaPar(lst):
    for v in lst:
        if v % 2 == 0:
            pares.append(v)
    print('Somando os valores pares: {}'.format(pares), end = '')
    print(', temos: {}'.format(sum(pares)))
    

sorteia(numeros)
somaPar(numeros)