'''Escrava um programa para aprovar o empréstimo bancário para a
compra de uma casa. Pergunte ovalor da casa, o salário do comprador
e em quantos anos ele vai pagar.
A prastação mensal, não pode exceder 30% do salário ou então o
empréstimo será negado.'''

valor_casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Quanto é o seu salário: R$'))
tempo = int(input('Em quantos anos você quer pagar: '))

prestacao = valor_casa / (tempo * 12)

if prestacao <= salario * 0.30:
    print('Você pode fazer este emprestimo \n\tValor da prestação: R${:.2f}'.format(prestacao))
elif prestacao > salario * 0.3:
    print('Você não pode fazer esse emprestimo \n\tValor da prestação: R${:.2f}'.format(prestacao))