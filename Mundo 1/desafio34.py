salario = float(input('Digite seu salário: '))

cores = {'limpa':'\033[m',
         'verde':'\033[4;32m',
         'vermelho':'\033[4;31m'
}

if(salario > 1250):
    salario_novo = salario * 1.10
if(salario <= 1250):
    salario_novo = salario * 1.15

print('Para este salario {}R${:.2f}{} esse é seu novo salário: {}R${:.2f}{}'.format(cores['vermelho'], salario, cores['limpa'], cores['verde'], salario_novo, cores['limpa']))