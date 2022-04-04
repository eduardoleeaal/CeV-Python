'''Cria um programa
que vai ler vários
números a colocar am
uma lista.
Depois disso. cria duas
listas extras que vÃo
conter apanas os
valoras paras e os
valoras imparas
digitados.
respectivamente.
Ao final. mostra o
conteúdo das três
listas geradas.'''
numeros = list()
pares = list()
impares = list()
while True:
    numeros.append(int(input('Digite um numero: ')))  
    print('Deseja continuar? ')
    pergunta = str(input('--> ')).strip().upper()[0]
    if pergunta in 'Nn':
        break  
for i, v  in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 != 0:
        impares.append(v)      
print('-=-' * 15)
print(f'A lista de todos os numeros é: {numeros}')
print(f'A lista de pares: {pares}')
print(f'A lista de impares: {impares}')    
