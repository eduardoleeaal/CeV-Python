'''Cria um programa
qua tenha uma FunSão
Fatorial() que receba
dois parâmatros: o
primeiro que indique o
número a calcular com
outro chamado show,
que será um valor lógico
(opcional) indicando sa
será mostrado ou não
na tela o processo de
cálculo do fatorial.
https://prnt.sc/fLKx0nrqjIGW
'''
def fatorial(num, show=False):
    """
    Função para calcular fatorial
    :param num: Numero a ser calculado
    :param show: Mostrar como é feito
    :return: Retorna o resultado do fatorial"""
    print('~~' * 20)
    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show:
        c = num
        f = 1
        print('  Calculando {}! → '.format(num), end='')
        for c in range(num, 0, -1):
            print('{}'.format(c), end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
            f *= c
    return f

print(fatorial(5, show = True))
