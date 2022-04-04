'''Cria um programa
que vai ler vários
números a colocar am
uma lista.
Depois disso. mostra:
A) Quantos números
foram digitados.
B) A lista da valoras.
ordenada da forma
decrascente.
C) Sa o valor 5 foi
digitado e está ou não
na lista.'''
numeros = list()
while True:
    numeros.append(int(input('Digite um numero: ')))  
    
       
    print('Deseja continuar?')
    pergunta = str(input('--> ')).strip().upper()[0]
    if pergunta in 'Nn':
        break
    
print(f'Quantidade de numeros digitados: {len(numeros)}')
numeros.sort(reverse=True)
print(f'Lista organizada invertida: {numeros}')
if 5 in numeros:
    print('O numero 5 apareceu!')
else:
    print('O numero 5 não apareceu!')   