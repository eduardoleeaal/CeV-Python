'''Faça um programa
que tanha uma Função
chamada ficha(), que
receba dois parâmatros
opcionais: o nome da um
jogador a quantos gols
ele marcou.
O programa daverá ser
capaz de mostrar a
ficha do jogador, mesmo
que algum dado não
tenha sido informado
corretamente.
https://prnt.sc/V9QfgKy-y6fN
'''

def ficha(nome = '', gols = 0):
    """
    Cadastro de Jogadores
    :param nome: Nome do jogador
    :param gols: Gols no campeonato
    """
    print('-' * 20)
    print(f'Nome do jogador: {nome}')
    print(f'Gols no campeonato: {gols}')
    if nome != '':
        print(f'O jogador {nome}, fez {gols} gol(s) no campeonato.')
    else:
        print(f'O jogador <desconhecido> fez, {gols} gol(s) no campeonato.')
    
n = str(input("Nome do jogador: "))
g = str(input("Gols do jogador: "))   
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols = g)
else:
    ficha(n, g)
