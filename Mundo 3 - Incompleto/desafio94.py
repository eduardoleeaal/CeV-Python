'''Crie um programa
que leia noma. Sexo e
idada da várias
passoas.guardando
os dados de cada
passoa em um
dicionário a todos os
dicionários em uma
lista. No final, mostra:
A) Quantas passoas
foram cadastradas
B) A média da idada do
grupo.
Ci Uma lista com todas
as mulheras.
D) Uma lista com todas
as passoas com idada
acima da média.

https://prnt.sc/QHXTvG2Cxtqt
'''
from time import sleep
cores = {'limpa':'\033[m',
         'vermelho':'\033[4;31m'}
dados = dict()
pessoas = list()
mulheres = list()
acima_idade = list()
soma = 0
while True: 
    dados['nome'] = str(input('Digite seu nome: ')).strip()
    dados['idade'] = int(input('Digite sua idade: '))
    dados['sexo'] = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
    if dados['sexo'] in 'Ff':
        mulheres.append(dados['nome'])
    soma += dados['idade']
    pessoas.append(dados.copy())
    dados.clear()

    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
media = soma / len(pessoas)
sleep(1)
print(f'{cores["vermelho"]}PROCESSANDO....{cores["limpa"]}')
sleep(1)
print('-=-' * 20)
print(f'-> O grupo tem {len(pessoas)} pessoas')
print(f'-> A media de idade do grupo é: {media}')
print(f'-> As mulheres cadastradas foram: {mulheres}')
print(f'-> Lista de pessoas acima da media de idade: ')
for i, k in enumerate(pessoas):
    if pessoas[i]['idade'] > media:
        print()
        print(f'  Nome = {pessoas[i]["nome"]}; sexo = {pessoas[i]["sexo"]}; idade = {pessoas[i]["idade"]}')
print(f'\n{cores["vermelho"]}<< ENCERRANDO >>{cores["limpa"]}\n')
