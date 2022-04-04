'''Faça um programa
que leia nome e peso
da várias passoas.
guardando tudo em
uma lista. 
No final.
mostre:
A) Quantas pessoas
Foram cadastradas.
B) Uma listagam com as
passoas mais pesadas.
C) Uma listagam com as
passoas mais leves.'''
temp = list()
princ = list()
maior = menor = 0

while True: 
    temp.append(str(input('Digite seu nome: ')))
    temp.append(float(input('Digite seu peso: ')))
    if len(princ) == 0: 
        maior = menor = temp[1]
    else:
        if temp[1] > maior: 
            maior = temp[1]
        if temp[1] < menor: 
            menor = temp[1]
            
    princ.append(temp[:])
    temp.clear()
    print('Deseja continuar?')
    r = str(input('--> ')).upper().strip()[0]
    if r in 'Nn':
        break
print('-=-' * 30)
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f'O menor peso foi de {menor} Kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}')
print(f'O maior peso foi de {maior} Kg. Peso de ', end = '')
for p in princ: 
    if p[1] == maior: 
        print(f'{p[0]}')