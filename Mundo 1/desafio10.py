carteira = float(input('Digite quanto dinheiro você tem: R$'))

valor = carteira / 3.27

print('Com R${:.2f} você pode comprar US${:.2f}'.format(carteira, valor))