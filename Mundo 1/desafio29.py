vel = float(input('Digite a velocidade do carro: '))

if(vel > 80):
    multa = (vel - 80) * 7
    print('Você foi multado em R${:.2f} por excesso de velocidade! \nVelocidade maxima permitida: 80Km/h'.format(multa))
else:
    print('Velocidade tranquila hein')