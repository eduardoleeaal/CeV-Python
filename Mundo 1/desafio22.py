nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiusculas: {}'.format(nome.upper()))
print('Seu nome em minusculas: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} Letras'.format(len(nome) - nome.count(' ')))
dividido = nome.split()
print('Seu primeiro nome é {} e ele tem {} Letras'.format(dividido[0], len(dividido[0])))
