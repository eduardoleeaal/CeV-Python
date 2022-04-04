'''Rafaça o DESAFIO 009. mostrando a tabuada da um númaro que o usuário ascolher.
só que agora utilizando um laço for.'''

n1 = int(input('Digite um numero: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n1, c, n1 * c))