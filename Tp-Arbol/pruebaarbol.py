from tdaarbol import NodoArbol, busqueda, eliminar, inorden, altura
from tdaarbol import postorden, preorden, insertar, reemplazar, act_altura
from tdaarbol import balancear, rot_doble, rot_simple
import random
r = None
r = insertar(r, 4)
r = insertar(r, 6)
r = insertar(r, 3)
r = insertar(r, 10)
r = insertar(r, 1)
r = insertar(r, 8)
r = insertar(r, 15)
r = insertar(r, 12)
r = insertar(r, 5)
preorden(r)
# 4,6,3,10,1,8,15,12,5

# ej1 TERMINAR
'''r = None
for i in range(0, 10):
    r = insertar(r, random.randint(0, 100))'''
# Parte A
print('Barrido preorden:')
preorden(r)
print('Barrido inorden:')
inorden(r)
print('Barrido postorden:')
postorden(r)
# Parte B
'''n = 40
if busqueda(r, n) is None:
    print('El numero no se encuentra en el arbol')
else:
    print('EL numero se encuentra en el arbol')'''
# Parte C TERMINAR
'''for i in range(0, 3):
    dato = int(input('Ingrese el numero que desea eliminar:'))
    eliminar(r, dato)
    preorden(r)'''
# Parte D
'''aux = altura(r.izq)
print('Altura del arbol izquierdo ' + str(aux))
aux1 = altura(r.der)
print('Altura del arbol derecho ' + str(aux1))'''
# Parte E


# ej5
'''r = None
"True heroe, false villano"
super = ["Ironman ", "Spiderman ", "CapitanAmerica ", "Dr.Strange ",
        "Hulk ", "BlackPanter "]
for elemento in super:
    r = insertar(r, random.choice(super) + str(random.choice([True, False])))
preorden(r)'''
# Parte D
