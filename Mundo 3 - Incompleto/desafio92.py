'''Cria um programa
que leia nome, ano de
nascimento e cartaira
da trabalho e
cadastre-os (com
idade) em um dicionário
se por acaso a CTPS
For diferenta de ZERO,
o dicionário receberá
também o ano de
contratação e o
salário. Calcula e
acrescente além da
idade com quantos
anos a pessoa vai se
aposentar.

35 anos até se aposentar'''

from datetime import datetime

pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
pessoa['Idade'] = datetime.now().year - nascimento
pessoa['CTPS'] = int(input('CTPS [0 se não tiver]: '))
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentar'] = pessoa['Idade'] + ((pessoa['Contratação'] + 35) - datetime.now().year)
print('-=-' * 20)
for k, v in pessoa.items():
    print(f'    -->{k} tem valor {v}.')