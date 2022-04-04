# https://prnt.sc/26n2bkp
nome = str(input('Digite seu nome: ')).strip()

dividir = nome.split()

print('Seu nome completo é: {}'.format(nome))
print('Seu primeiro nome é: {}'.format(dividir[0]))
print('Seu ultimo nome é: {}'.format(dividir[len(dividir) - 1]))
print(len(dividir))