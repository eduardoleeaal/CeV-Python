'''Cria um programa
qua tenha a função
leialnt(), que vai
Funcionar da forma
semelhanta à função
input() do Python. só
que fazendo a validação
para aceitar apenas um
valor numérico.
Ex:
n= leialnt('Digite um n')
https://prnt.sc/lZScDsMtfYag
'''

def leiaInt(par):
    print(par, end = '')
    t = input()
    while not t.isnumeric(): 
        print('\033[0;31mValor Incorreto, Digite um valor inteiro válido!\033[m')
        t = input('Digite um Numero: ')
    return int(t)


n = leiaInt('Digite um Numero: ')
print(f'Você acabou de digitou o valor: {n}')
