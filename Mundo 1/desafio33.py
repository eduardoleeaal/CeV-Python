n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
maior_numero = n1
menor_numero = n1
# Verificando o maior
if(n2 > n1):
    maior_numero = n2
if(n2 < n1):
    menor_numero = n2
# Verificando o menor
if(n3 > n2 and n3 > n1):
    maior_numero = n3
if(n3 < n2 and n3 < n1):
    menor_numero = n3

print('O maior numero: {}'.format(maior_numero))
print('O menor numero: {}'.format(menor_numero))