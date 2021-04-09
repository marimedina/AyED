from tdapiladin import Pila, apilar, desapilar, pila_llena
from tdapiladin import pila_vacia, tamanio, NodoPila, cargautomatica

p = Pila()
pp = Pila()
paux = Pila()

'''cargautomatica(p)
print(p.tamanio)
num = 5
cont = 0
while not pila_vacia(p):
    dato = desapilar(p)
    if dato == num:
        cont += 1
    apilar(paux, dato)
print('Cantidad de ocurrencias:', cont)
while not pila_vacia(paux):
    apilar(p, desapilar(paux))'''

cargautomatica(p)
print(p.tamanio)
while not pila_vacia(p):
    aux = desapilar(p)
    if aux % 2 == 0:
        apilar(pp, aux)
    else:
        aux
