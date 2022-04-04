"""Adapte o código do
desafio 107, criando uma
função adicional
chamada moeda() que
consiga mostrar os
valores como um valor
monetário formatado."""

from desafio107 import moeda

p = float(input("Digite um valor: "))
print(f'A metade de {p:.2f}: {moeda.metade(p):.2f}')
print(f'O dobro de {p:.2f}: {moeda.dobro(p):.2f}')
print(f'Aumentando 10% de {p:.2f}: {moeda.aumentar(p, 10):.2f}')
print(f'Reduzindo 13% de {p:.2f}: {moeda.diminuir(p, 13):.2f}')