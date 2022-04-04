# https://prnt.sc/26ox0e0
from random import choice

c = {    'li':'\033[m',
         've':'\033[4;32m',
         'ver':'\033[4;31m',
    }

escolha = str(input('Escolha Pedra, Papel ou Tesoura: ')).strip()
bot = choice(['PEDRA', 'PAPEL', 'TESOURA'])

if(escolha.upper() == bot):
    print('O Jogo empatou, com você escolhendo {}{}{} e o bot escolhendo {}{}{}'.format(c['ve'],escolha.upper(), c['li'],c['ve'], bot,c['li']))
else:
    if(escolha.upper() == 'PAPEL' and bot == 'PEDRA'):
        print('Você ganhou escolhendo {}{}{} e o bot {}{}{}'.format(c['ve'],escolha.upper(), c['li'],c['ver'], bot,c['li']))
    elif(escolha.upper() == 'TESOURA' and bot == 'PAPEL'):
        print('Você ganhou escolhendo {}{}{} e o bot {}{}{}'.format(c['ve'],escolha.upper(), c['li'],c['ver'], bot,c['li']))
    elif(escolha.upper() == 'PEDRA' and bot == 'TESOURA'):
        print('Você ganhou escolhendo {}{}{} e o bot {}{}{}'.format(c['ve'],escolha.upper(), c['li'],c['ver'], bot,c['li']))
    else:
        print('Você perdeu escolhendo {}{}{} e bot {}{}{}'.format(c['ver'],escolha.upper(), c['li'],c['ve'], bot,c['li']))
