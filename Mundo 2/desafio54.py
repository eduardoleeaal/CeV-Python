'''Cria um programa
que leia o ano de
nascimanto de sete
pessoas. No final.
mostre quantas
passoas ainda não
atingiram a maioridada
e quantas já SÃO
maiores.'''
from datetime import date

maior = 0
menor = 0
for c in range(0, 7):
    ano = int(input('Digite o ano do seu nascimento: '))
    idade = date.today().year - ano
    if(idade >= 21):
        maior += 1
    else:
        menor += 1
print('Quantos já atingiram a maioridade: {}'.format(maior))
print('Quantos ainda são de menor: {}'.format(menor))