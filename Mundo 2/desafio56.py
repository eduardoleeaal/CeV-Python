'''Desenvolva um programa qua leia o nome, idade e sexo de 4 pessoas. 
No final do programa. Mostre:
- A média da idade do
grupo.
- Qual é o nome do
homem mais velho.
- Quantas mulheres
têm menos de 20
anos.'''
media = 0
mais_velho = 0
soma = 0
count_F = 0
nome_v = ''
for c in range(0, 4):
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (M/F): ')).strip()
    print('-=-' * 15)
    soma += idade
    media = soma / 4
    if(idade < 20 and sexo.upper() == 'F'):
        count_F += 1
    if(idade > mais_velho and sexo.upper() == 'M'):
        mais_velho = idade
        nome_v = nome
print('Nome do Homem mais velho: {}'.format(nome_v))
print('Media de idade: {:.0f} Anos'.format(media))
print('Quantidade de mulheres com menos de 20 anos: {}'.format(count_F))
print('-=-' * 20)