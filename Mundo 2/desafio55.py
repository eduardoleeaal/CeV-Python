'''Faça um programa
que leia o peso de
cinco passoas. No
Final. mostra qual Foi o
maior ao menor peso
lidos.'''

for c in range(0, 5):
    peso = float(input('Digite o seu peso: '))
    if c == 1:
        maior = c
        menor = c
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))