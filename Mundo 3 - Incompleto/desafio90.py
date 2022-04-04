'''Fasa um programa
que leia noma a média
da um aluno.
guardando também a
EituaSão am um
dicionário. No final.
mostre o conteúdo da
estruturana tela.'''

aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Media de {aluno["Nome"]}: '))
print('-=-' * 15)
if aluno['Média'] >= 7:
    aluno['Situacao'] = "Aprovado"
elif aluno['Média'] >= 6 and aluno['Média'] < 7:
    aluno['Situacao'] = "Recuperação"
else:
    aluno['Situacao'] = "REPROVADO"
for k, v in aluno.items():
    print(f'    --> {k} é igual a {v}')
