'''Cria um programa que leia o nome e o preço da vários produtos.
O programa daverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.'''
from time import sleep
total = prod1000 = valortot= cont = 0
nome_barato = ' '
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    valor = float(input('Digite o valor do produto: R$'))
    print('-=-' * 20)
    cont += 1
    if cont == 1:
        prodbara = valor
        confi = 1
    if valor <= prodbara and confi == 1:
        prodbara = valor
        nome_barato = nome   
    if valor > 1000:
        prod1000 += 1
    valortot += valor
    pergunta = ' '
    while pergunta not in 'SsNnYy':
        print('Deseja continuar?')
        pergunta = str(input('-->')).strip().upper()[0]
    if pergunta not in 'Ss':
        print('ENCERRANDO')
        sleep(1)
        break
print('---' * 20)
print(f'Valor total gasto: R${valortot:.2f}')
print(f'Produtos que passaram de R$1000: {prod1000}')
print(f'Nome do produto mais barato é {nome_barato} que custa R${prodbara:.2f}')
