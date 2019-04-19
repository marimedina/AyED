from tdapila import apilar, desapilar, pila_llena, pila_vacia, tamanio, cima
from tdapila import pila, cargautomatica
import random
p = pila()
p1 = pila()
pp = pila()
pi = pila()
'''cargautomatica(p)
while not pila_vacia(p):
    aux = desapilar(p)
    if aux % 2 == 0:
        apilar(pp, aux)
    else:
        apilar(pi, aux)
print('pila par')
while not pila_vacia(pp):
    print(desapilar(pp))'''

#ej2
cargautomatica(p)
while not pila_vacia(p):
    aux = desapilar(p)
    if aux % 2 == 0:
        apilar(pp, aux)
    else:
        desapilar(p, aux)
        
