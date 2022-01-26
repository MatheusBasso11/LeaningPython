from math import radians, sin, cos, tan
ang = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(ang))
print('O angulo de {} tem o SENO de {:.2f}'.format(ang, seno))
cosseno = cos(radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cosseno))
tangente = tan(radians(ang))
print('O ângulo {} tem a TANGENTE de {:.2f}'.format(ang, tangente))
