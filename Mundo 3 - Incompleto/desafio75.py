'''Dasenvolva um
programa que leia
quatro valoras palo
taclado a guarde-os
em uma tupla. No final.
mostra:
A) Quantas vazes
aparecau o valor 9.
B) Em que posião foi
digitado o primairo
valor 3.
C) Quais foram os
númaros paras.'''
tupla = (int(input('Digite um numero: ')),
         int(input('Digite outro numero: ')), 
         int(input('Digite mais um numero: ')), 
         int(input('Digite o ultimo numero: ')))
print(f'Quantidade de noves: {tupla.count(9)}')
if 3 in tupla:
    print(f'Primeiro numero 3 na {tupla.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares são: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
