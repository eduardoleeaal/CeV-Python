'''Cria um programa
onda o usuário possa
digitar vários valoras
numéricos a
cadastre-os em uma
lista. Caso o número já
axista lá dentro. cla
nÃO será adicionado.
No Final, serÃO
axibidos todos os
valoras únicos
digitados. am ordam
crescente.'''
numeros = []

while True:
    n = int(input('Digite um numero: '))
    if n not in numeros:
        numeros.append(n)
        print('\033[4;32mValor adicionado!\033[m')
    else:
        print('\033[4;31mValor duplicado, Não adicionado\033[m')  
    print('Quer continuar?')
    r = str(input('--> ')).upper().strip()[0]
    if r in 'Nn':
        break
numeros.sort()
print(numeros)
    