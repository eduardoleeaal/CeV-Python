'''Cria um programa
onde o usuário possa
digitar cinco váloras
numéricos a
cadastra-os em uma
lista. já na posisão
corrata da inserSão
(sem usar o sort(0).
No final. mostra a lista
ordenada na tala.'''
numeros = list()
for c in range(0, 5):
    n = int(input('Digite um numero: '.format(c + 1)))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Adicionado na posição {pos + 1}')
                break
            pos += 1
            
print(numeros)