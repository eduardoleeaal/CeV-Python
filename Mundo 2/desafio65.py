'''Crie um programa
que leia vários
números inteiros palo
teclado. No final da
exec. Mostre a
média entre todos os
valoras e qual Foi o
maior e o menor
valoras lidos. O
programa deva
perguntar ao usuário
sa ele quer ou não
continuar a digitar
valoras.'''

soma = quant = media = 0
resposta = 'S'
while resposta in 'Ss':
    n1 = int(input('Digite um numero: '))
    soma += n1    
    quant += 1
      
    if quant == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        elif n1 < menor:
            menor = n1    
    print('Deseja continuar?')
    resposta = str(input('→ ')).strip().upper()[0]

media = soma / quant
print('A média de {} numeros é {}'.format(quant, media))
print('O menor numero é {}'.format(maior))
print('O menor numero é {}'.format(menor))