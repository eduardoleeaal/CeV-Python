from random import choice

alunos = [''] * 4

alunos[0] = input('Digite o nome do primeiro aluno: ')
alunos[1] = input('Digite o nome do segundo aluno: ')
alunos[2] = input('Digite o nome do terceiro aluno: ')
alunos[3] = input('Digite o nome do quarto aluno: ')

aluno_sorteado = choice(alunos)

print ('=' * 15)
print('O aluno sorteado é: {}'.format(aluno_sorteado))
print ('=' * 15)
