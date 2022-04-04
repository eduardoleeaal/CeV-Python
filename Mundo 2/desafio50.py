'''Desenvolva um
programa que leia seis
números inteiros a
mostre a soma apenas
daquelas que forem
pares. Se o valor
digitado for impar.
desconsidere-o.'''
soma = 0
for c in range(0, 6):
    n1 = int(input('Digite o {}° numero: '.format(c + 1)))
    if(n1 % 2 == 0):
        soma += n1
print('Soma de todos os pares: {}'.format(soma))