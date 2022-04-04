from math import hypot
from math import sqrt
from math import pow

ca = float(input('Digite o tamanho do cateto Oposto: '))
co = float(input('Digite o tamanho do Cateto Adjacente: '))

hip = hypot(ca, co)                     # Calculo por função
hipo = (ca ** 2 + co ** 2) ** (1/2)     # Calculo por matematica
hipot = sqrt(ca ** 2 + co ** 2)         # Função / Matematica
hipote = sqrt(pow(ca, 2) + pow(co, 2))  # Funções

print('A hipotenusa é: {}'.format(hip))
print('A hipotenusa é: {}'.format(hipo))
print('A hipotenusa é: {}'.format(hipot))
print('A hipotenusa é: {}'.format(hipote))