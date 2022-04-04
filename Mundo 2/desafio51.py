'''Desenvolva um
programa que leia o
primeiro termo e a
razão de uma PA. No
final, mostra os 10
primeiros termos
dessa progressão.'''

# pt = int(input('Digite o primeiro termo: '))         # 1
# pa = int(input('Digite a razão: '))                  # 2
# for c in range(0, 10):
#     print(pt, end=' -> ')                            # --> 1         3           5           7
#     pt += pa                                         # --> 3         5           7           9
# print('ACABOU')

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão

for c in range(primeiro, décimo + razão, razão):
    print('{}'.format (c), end=' -> ')
print('ACABOU')
