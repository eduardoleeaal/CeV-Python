'''Malhore o DESAFIO
061. Perguntando para
o usuário se ele quer
mostrar mais alguns
termos. O programa
encerra quando ela
disser que quer
mostrar 0 termos.'''

pt = int(input('Digite o primeiro termo: '))         # 1
pa = int(input('Digite a razão: '))                  # 2
c = 1
quant = 0
mais = 10
while mais != 0:
    quant += mais
    while c <= quant:
        print(pt, end=' → ')                            # --> 1         3           5           7
        pt += pa                                         # --> 3         5           7           9
        c += 1
    mais = int(input('\nQuantos termos você quer mostrar a mais? '))
print('ACABOU')