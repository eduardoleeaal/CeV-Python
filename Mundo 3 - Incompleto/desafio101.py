'''Crie um programa
que tenha uma Função
chamada voto() que
vai raceber como
parâmetro o ano de
nascimento de uma
pessoa, retornando
um valor literal
indicando se uma
pessoa tem voto
NEGADO, OPCIONAL ou
OBRIGATÓRIO nas
eleições.
https://prnt.sc/gDRj2mN6ccDJ
'''

def voto(ano):
    """
    -> Função para ver se a pessoa precisa votar!
    :param ano: Ano de nascimento
    :return: status de voto e idade
    """
    import time
    idade = int(time.strftime("%Y")) - ano
    if idade < 16:
        stats = 'Você NÃO PODE votar!'
    elif 16 <= idade < 18 or idade > 65:
        stats = 'O seu voto é OPCIONAL!'
    else:
        stats = 'Você é OBRIGADO a votar!'
    return stats, idade


n = int(input("Digite o seu ano de nascimento: "))
x, y = voto(n)
print(f'Com {y} anos, {x}')
