'''Faça um programa
que leia 5 valoras
numéricos a guarde-os em uma lista.
No final, mostra qual
Foi o maior ao manor
valor digitado a as
suas respactivas
posisõas na lista.'''

numeros = list()
mai = 0
men = 0
for count in range(0, 5):
    numeros.append(int(input('Digite um valor para a posição {}: '.format(count + 1))))
    if count == 0:
        mai = men = numeros[count]
    else:
        if numeros[count] > mai:
            mai = numeros[count]
        if numeros[count] < men:
            men = numeros[count]
print('-=-' * 15)
print(f'Lista completa: {numeros}')
print('O maior numero é o {} na posição '.format(max(numeros)), end='')
for i, v in enumerate(numeros):
    if v == mai:
        print(f'{i + 1}', end=' ')
print('\nO menor numero é o {} na posição '.format(min(numeros)), end='')
for i, v in enumerate(numeros):
    if v == men:
        print(f'{i + 1}', end=' ')