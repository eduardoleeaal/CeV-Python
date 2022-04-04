'''Faça um um mini-
sistema qua utiliza o
Interactive Help do
Python. O usuário vai
digitar o comando ao
manual vai aparecer.
Quando o usuário digitar
a palavra 'FIM', o
programa sa encerrará.

OBS: use cores.
https://prnt.sc/R9hBVycJ7spq
'''

from time import sleep


cores = {
    'limpa': '\033[m',
    'verde': '\033[0;32m',
    'BReVE': '\033[0;30;42m',
    'BReRX': '\033[0;30;45m',
    'BReAZ': '\033[0;30;44m',
    'vermelho': '\033[0;31m'
}


def ajuda(par):
    """
    :param par: Comando para ser analisado
    :return: não retorna nada
    """
    print(f'{cores["BReAZ"]}~' * (len(par) + 36))
    print(f"  Acessando o manual do comando '{par}'")
    print(f'~' * (len(par) + 36))
    print(f'{cores["limpa"]}', end='', flush=True)
    sleep(0.3)
    print(f'{cores["BReRX"]}')
    help(par)
    print(f'{cores["limpa"]}', end='', flush=True)
    sleep(0.3)


while True:
    print(f'{cores["BReVE"]}~' * (len('Sistema de Ajuda PyHELP') + 4))
    print(f'  Sistema de Ajuda PyHELP')
    print('~' * (len('Sistema de Ajuda PyHELP') + 4))
    print(f'{cores["limpa"]}', end='')

    pal = str(input('Função ou biblioteca > ')).strip()
    if pal.lower() in "fim":
        sleep(0.3)
        print(f'{cores["vermelho"]}FINALIZANDO...{cores["limpa"]}')
        break
    ajuda(pal)

