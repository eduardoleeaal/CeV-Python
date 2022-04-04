'''Faça um programa
que tenha uma Função
chamada área()), qua
raceba as dimansões
da um terreno
retangular (largura a
comprimento) e
mostre a área do
terreno.
https://prnt.sc/5tlf-eK1ODN6
'''
def área(a, b):
    area = a * b
    print(f'A área de um terreno {a}x{b} é de {area}m²')
    

lar = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
área(lar, comp)
