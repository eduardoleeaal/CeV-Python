'''Faça um programa
que leia um número
qualquer a mostra o
seu fatorial.
Ex:
5 = 5x4x3x2x1=120'''

n1 = int(input('Digite um numero inteiro para calcular o fatorial: '))
c = n1
f = 1
print('Calculando {}! → '.format(n1), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x 'if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))


# Com a estrutura For
nu = int(input("Digite um numero para calcular o fatorial: "))
n = nu
for i in range(n):
    if n != i and i != 0:
        n *= i 
print(f'Resultado de {nu}!: {n}')
