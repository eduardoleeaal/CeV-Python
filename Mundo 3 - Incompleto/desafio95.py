'''Aprimora o DESAFIO
093 para que cla
funciona com vários
jogadoras. incluindo
um sistama da
visualizaSÃo de
detalhas do
aprovaitamento da
cadajogador.

https://prnt.sc/zv619GWdnjiP
'''
time = list()
jogador = dict()
gols = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Digite o nome do jogador: '))
    partidas = int(input('Digite a quantidade de partidas: '))
    gols.clear()
    for i in range(partidas):
        gols.append(int(input(f'Gols na partida {i + 1}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N': 
        break
print('-=-' * 20)
print('cod', end = '')
for i in jogador.keys():
    print(f'{i:<15}', end = '')
print()
print('-' * 40)
for k, v in enumerate(time): 
    print(f'{k:>3} ',end = '')
    for d in v.values():
        print(f'{str(d):<15}',end = '')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador: '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO!, Não existe jogador com o codigo {}'.format(busca))
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')