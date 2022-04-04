'''Faça um programa
que calcula a soma
antra todos os
númaros impares que
SÃo múltiplos de três a
que se encontram no
intervalo dalaté 500.'''

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de {} numeros é: {}'.format(cont, soma))