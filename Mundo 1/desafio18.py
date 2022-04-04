from math import sin, cos, tan, radians

ang = float(input('Digite o ângulo que você deseja: '))

sen = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print('O ângulo {:.0f}° tem o SENO: {:.2f}'.format(ang, sen))
print('O ângulo {:.0f}° tem o COSSENO: {:.2f}'.format(ang, coss))
print('O ângulo {:.0f}° tem a TANGENTE: {:.2f}'.format(ang, tang))