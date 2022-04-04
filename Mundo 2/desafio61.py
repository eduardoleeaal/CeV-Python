'''Rafaça o DESAFIO
051. Lendo o primeiro
termo e a razão da uma
PA. Mostrando os 10
primeiros termos da
progressão usando a
estrutura while.'''

pt = int(input('Digite o primeiro termo: '))         # 1
pa = int(input('Digite a razão: '))                  # 2
c = 0
while c < 10:
    print(pt, end=' → ')                            # --> 1         3           5           7
    pt += pa                                         # --> 3         5           7           9
    c += 1
print('ACABOU')