# https://prnt.sc/26owzv9

print('-=-' * 20)
print('Analisador de triangulo')
print('-=-' * 20)


r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if(r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2):
    print('Os segmentos podem formar triangulo')
    if(r1 == r2 == r3):
        print('Triangulo equilátero')
    elif(r1 == r2 and (r1 != r3 or r2 != r3)):
        print('Triaguno Isósceles')
    elif(r1 != r2 != r3):
        print('Triangulo Escaleno')
else:
    print('Os segmentos não podem formar triangulos')