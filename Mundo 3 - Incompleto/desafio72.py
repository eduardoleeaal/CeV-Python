'''Crie um programa
que tenha uma tupla
totalmanta
preenchida com uma
contagam por
extenso, de zero até
vinte.
Seu programa daverá
ler um numero pelo
teclado (0 e 20)
e mostrá-lo por
extenso.'''
while True:
    numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'
    print('-=-' * 10)
    valor = int(input('Digite um numero de 0 à 20: '))
    while valor < 0 or valor > 20:
        valor = int(input('Você digitou um valor Incorreto! Digite um numero de 0 à 20: '))
    print(f'Você digitou o numero {numeros[valor]}')
    print('-=-' * 10)
    while True:
        print('Você quer continuar?')
        pergunta = str(input('--> ')).upper().strip()[0]
        if pergunta in 'SsNn':
            break
    if pergunta in 'Nn':
        break
print('-=-' * 10)
print('FIM!')