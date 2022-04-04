# https://prnt.sc/26ox0a8

c = {    'li':'\033[m',
         've':'\033[4;32m',
         'ver':'\033[4;31m',
         'ama':'\033[4;33m',
         'azul': '\033[4;34m'
}

valor = float(input('Digite o valor do item: '))
print('{}[1] Dinheiro / Cheque = 10% de desconto \n[2] 1x Cartão = 5% de desconto \n[3] 2x Cartão = Sem Juros \n[4] 3x + Cartão = 20% Juros{}'.format(c['ama'], c['li']))
metodo = int(input('Digite o numero do seu método de pagamento: '))

if(metodo == 1):
    print('Você escolheu pagar por {}Dinheiro / Cheque{} e receberá {}10% de desconto{}'.format(c['ve'], c['li'], c['ve'], c['li']))
    valor_computado = valor * 0.90
elif(metodo == 2):
    print('Você escolheu pagar por {}Cartão à vista{} e receberá {}5% de desconto{}'.format(c['ve'], c['li'], c['ve'], c['li']))
    valor_computado = valor * 0.95
elif(metodo == 3):
    print('Você escolheu pagar por {}Cartão em 2x{} e pagara o {}preço normal{} do produto'.format(c['ve'], c['li'], c['ve'], c['li']))
    valor_computado = valor * 1
elif(metodo == 4):
    print('Você escolheu pagar em {}3x ou mais no cartão{} e terá {}20% de juros{}'.format(c['ve'], c['li'], c['ver'], c['li']))
    valor_computado = valor * 1.20

if(metodo in [1, 2, 3]):
    print('{}Preço final:{} {}R${}{}'.format(c['azul'], c['li'], c['ve'], valor_computado, c['li']))
elif(metodo == 4):
    print('{}Preço final:{} {}R${}{}'.format(c['azul'], c['li'], c['ver'], valor_computado, c['li']))