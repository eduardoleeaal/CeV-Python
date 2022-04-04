'''Cria um programa que leia dois valores a mostra um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa 
Seu programa daverá realizar a operação solicitada em cada caso.'''

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
print('-=-' * 20, end='')
print("""
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa""")
escolha = int(input('Escolha uma opção: '))
while escolha != 5:
    if(escolha == 1):
        print('A soma de {} e {} é {}'.format(n1, n2, n1 + n2))
    elif(escolha == 2):
        print('O produto de {} e {} é {}'.format(n1, n2, n1 * n2))
    elif(escolha == 3):
        if(n1 > n2):
            print('Entre {} e {} o maior é {}'.format(n1, n2, n1))
        elif(n1 < n2):
            print('Entre {} e {} o maior é {}'.format(n1, n2, n2))
        else:
            print('{} e {} são iguais!')
    elif(escolha == 4):
        print('Você escolheu selecionar novos numeros!')
        n1 = float(input('Digite um numero: '))
        n2 = float(input('Digite outro numero: '))
    print('-=-' * 20)
    print("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos númaros
    [5] Sair do programa""")
    escolha = int(input('Escolha uma opção: '))
    print('-=-' * 20)

print('\033[4;31mFim do programa!\033[m')