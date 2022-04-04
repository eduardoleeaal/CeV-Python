'''Cria um programa
que garenciao
aprovaitamaento de um
jogador da futabol. 0
programa vai ler o
nome do jogador e
quantas partidas ele
jogou. Depois vailer a
quantidade da gols
feitos em cada
partida. No final, tudo
isso será guardado am
um dicionário.
incluindo o total de
gols faitos durante o
campaonato.
https://prnt.sc/ohX-X0qQidfx
'''

jogador = dict()
gols = list()
jogador['Nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input('Digite a quantidade de partidas: '))
for i in range(partidas):
    gols.append(int(input(f'Gols na partida {i + 1}: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=-' * 20)
print(jogador)
print('-=-' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 20)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for i, v in enumerate(gols):
    print(f'    => Na partida {i + 1}, fez {v} Gols.')
print(f'Foi um total de {jogador["total"]} gols.')