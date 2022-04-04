valor = float(input('Digite um valor em metros: '))

km      = valor / 1000
hm      = valor / 100
dam     = valor / 10
dc      = valor * 10
cent    = valor * 100
mili    = valor * 1000
print('-' * 12)
print('Valor em metros: {}, \n{}km, \n{}hm'.format(valor, km, hm))
print('{}dam, \n{}dm, \n{}cm, \n{}mm'.format(dam, dc, cent, mili))
print('-' * 12)