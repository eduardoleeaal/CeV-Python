altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))

area = altura * largura

#Cada litro de tinta pinta 2m²
litro = area / 2

print('Será ultilizado um total de {:.2f}l Litros de tinta para pintar uma parede de {}m²'.format(litro, area))