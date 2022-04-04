# https://prnt.sc/26n7rpa

distancia = float(input('Digite a distância da viagem: '))

if(distancia <= 200):
    valor = distancia * 0.50
    
else:
    valor = distancia * 0.45
    
print('Para uma viagem de {}Km, o valor da passagem é: R${:.2f}'.format(distancia, valor))