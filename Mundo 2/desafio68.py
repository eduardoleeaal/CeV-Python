'''Faça um programa
qua jogue par ou impar
com o computador. O
jogo só sará
interrompido quando o
jogador PERDER,
mostrando o total de
vitórias consecutivas
que ela conquistou no
Final do jogo.'''
from random import choice
from random import randint
#vit = 0
#    # bot = choice(['P', 'IÍ'])    
#    # while escolha not in 'PpIÍií':
#    #     escolha = str(input('Escolha Par ou Ímpar: ')).strip().upper()[0]
#    # print('---' * 20)
#    # if escolha not in bot:
#    #     print('\033[4;31mVocê perdeu!\033[m')
#    #     print('-=-' * 20)
#    #     break
#    # vit += 1
#    # print('\033[4;32mVocê ganhou!\033[m')
#    # print('-=-' * 20)
#    # escolha = 'a'
#print('Quantidade total de vitorias: {}'.format(vit))
#print('===' * 20)

vito = 0
while True:
    bot = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    total = jogador + bot
    tipo =' '
    while tipo not in 'PpIÍ':
        tipo = str(input('Par ou Ímpar: ')).strip().upper()[0]
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vito += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você venceu!')
            vito += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {vito} vezes')