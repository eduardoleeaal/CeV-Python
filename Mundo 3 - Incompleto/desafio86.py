'''Crie um programa
que cria uma matriz da
dimensão 3x3 a
preencha com valoras
lidos pelo teclado.

No Final. mostraa
matriz na tala. com a
FormatafÃo corrata.'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l + 1}, {c + 1}]: '))
print('-=-' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()