'''Faça um programa
que tenha uma Função
chamada escrava().
que receba um texto
qualquer como
parâmetro e mostre
uma mensagem com
tamanho adaptável.
Ex:
escrava('Olá. Mundo!')
Saida:
~~~~~~~~~~~~~~~~
   Olá. Mundo!
~~~~~~~~~~~~~~~~
https://prnt.sc/AnEO4jLkSuRw
'''
def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))
    
    
# Programa Principal
escreva('Eduardo Leal')
escreva('Olá, Mundo!')
escreva('CeV')
escreva('hm')