dias = int(input('Quantos dias fora ultilizados: '))
quilometragem = float(input('Quantos km foram rodados: '))

valor_total = dias * 60 + quilometragem * 0.15

print('O total a ser cobrado é: R${:.2f}'.format(valor_total))
