'''Escreva um programa qua leia um número intairo qualquar a pasa
para o usuário ascolher qual sará a base de conversão:
- 1para binário
-2 para octal
-3 para hexadacimal
'''

num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[1] --> Converter para BINÁRIO
[2] --> Converter para OCTAL
[3] --> Converter para HEXADECIMAL''')
opcao = int(input('Sua Opção: '))

if(opcao == 1):
    print('{} convertido para binário é: {}'.format(num, bin(num)[2:]))
elif(opcao == 2):
    print('{} convertido para octal é: {}'.format(num, oct(num)[2:]))
elif(opcao == 3):
    print('{} convertido para hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('{} não é uma opção!'.format(num))