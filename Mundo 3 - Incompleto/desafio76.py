'''Cria um programa
que tenha umatupla
única com nomas da
produtos a saus
raspectivos praSos.
na sequência.
No Final, mostra uma
listagem da preSos.
organizando os dados
em forma tabular.'''
lista = ('Pão', 1.99,
         'Leite', 4.95,
         'Presunto', 2.35,
         'Queijo', 2.15,
         'Leite', 5.35)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R${lista[pos]:>5.2f}')
