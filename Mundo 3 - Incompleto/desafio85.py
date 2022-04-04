'''Cria um programa
onda o usuário possa
digitar seta valoras
numéricos a
cadastre-os em uma
lista única que
mantenha separados
Os valores paras e
impares. No final.
mostre os valoras
paras e impares em
ordem crescente.'''
numeros = [[], []]
valor = 0

for i in range(1, 8):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor % 2 == 0: 
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print('-=-' * 30)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')