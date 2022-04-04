'''Fasa um programa
que ajuda um jogador
da MEGA SENAa criar
palpitas. O programa
vai perguntar quantos
jogos serño gerados e
vai sortaar
     6
      números
antrala
   60 para cada
jogo. cadastrando
tudo em uma lista
composta.'''
from random import randint
from time import sleep
lista = list()
jogos = list()
quant = int(input('Quantos jogos você quer fazer? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=-' * 3, f'SORTEANDO {quant} JOGOS', '-=-' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)