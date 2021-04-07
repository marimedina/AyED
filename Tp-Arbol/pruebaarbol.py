from tdaarbol import NodoArbol, busqueda, eliminar, inorden, altura
from tdaarbol import postorden, preorden, insertar, reemplazar, act_altura
from tdaarbol import balancear, rot_doble, rot_simple
from tdaarbol import *
import random



# FALTA

# 3 - Indice de Summerville
# 5 - Heroes/Villanos

'''
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
preorden(r)'''
# 4,6,3,10,1,8,15,12,5


# Ej 1 - Desarrollar un algoritmo que permita cargar 1000 numero enteros generados de manera
# aleatoria
'''
r = None
for i in range(0, 10):
    r = insertar(r, random.randint(0, 100))
'''

# Parte A - Realizar los barridos preorden, inorden y postorden sobre el arbol generado.
'''
print('Barrido preorden:')
preorden(r)
print('Barrido inorden:')
inorden(r)
print('Barrido postorden:')
postorden(r)
'''

# Parte B - Determinar si un numero esta cargado en el arbol o no.
'''
preorden(r)
n = 40
if busqueda(r, n) is None:
    print('El numero no se encuentra en el arbol')
else:
    print('EL numero se encuentra en el arbol')
'''

# Parte C - Eliminar tres valores del arbol.
'''
preorden(r)
for i in range(1, 4):
    dato = int(input('Ingrese el numero que desea eliminar:'))
    eliminar(r, dato)
preorden(r)
'''

# Parte D - Determinar la altura del subarbol izquierdo y del subarbol derecho.
'''
aux = altura(r.izq)
print('Altura del arbol izquierdo ' + str(aux))
aux1 = altura(r.der)
print('Altura del arbol derecho ' + str(aux1))
'''

# Parte E - Determinar si existen valores repetidos en el arbol
'''
preorden(r)
nodoRepetido(r)
'''

# Parte F - Contar cuantos numeros pares e impares hay en el arbol.
'''
preorden(r)
par, impar = numParImpar(r)
print('Numeros pares: ' + str(par), 'Numeros impares: ' + str(impar))
'''


#Ej 2 - Implementar un funcion que permita cargar una expresion
# matematica en un arbol binario
'''
# EXPRESION ((5+8)*2) + 5
def expresion(r=None):
    r = NodoArbol("+")
    r.der = NodoArbol(5)
    r.izq = NodoArbol("*")
    r.izq.der = NodoArbol(2)
    r.izq.izq = NodoArbol("+")
    r.izq.izq.izq = NodoArbol(5)
    r.izq.izq.der = NodoArbol(8)

    return r

raiz = expresion()
'''
#Parte A - Determine cual de los barridos muestra la expresion en el orden correcto.
'''
inorden(raiz)
'''

#Parte B - Resuelva la expresion matematica y muestre el resultado.
'''
def operacion(op, izq, der):
    resultado = 0
    if op == "+":
        resultado = izq + der
    elif op == "-":
        resultado = izq - der
    elif op == "*":
        resultado = izq * der
    elif opr == "/":
        resultado = izq / der

    return resultado

def calculo(raiz):
    if esHoja(raiz):
        return raiz.info
    else:
        return operacion(raiz.info, calculo(raiz.izq), calculo(raiz.der))

print('El resultado de la expresion es:')
print(calculo(raiz))
'''


# Ej 4 - Implementar un algoritmo que contemple dos funciones, la primera que devuelva el hijo
# derecho de un nodo y la segunda que devuelva el hijo izquierdo.
'''
r = None
for i in range(0, 10):
    r = insertar(r, random.randint(0, 100))
inorden(r)


print('Arbol derecho')
postorden(hijoDerecho(r))
print('Arbol izquierdo')
postorden(hijoIzquierdo(r))
'''


# ej5
'''
# Parte A - En cada nodo del arbol se almacenara un campo booleano que indica si es un heroe o un villano
r = None
"True heroe, false villano"
super = ["Ironman ", "Spiderman ", "CapitanAmerica ", "Dr.Strange ",
        "Hulk ", "BlackPanter "]


for elemento in super:
    r = insertar(r, random.choice(super) + str(random.choice([True, False])))
preorden(r)

# Parte B -

print('')
EsVillano(r)

# Parte C - Mostar todos los superheroes que empiezan con C

print('')
print('Superheroes que comienzan con C:')
superheroesConC(r)


# Parte D

#print('')
#print(cantidadSuperheroes(r))
'''


# Ej 7

r = None
for i in range(0, 6):
    r = insertar(r, random.randint(0, 100))
inorden(r)

print('')
nodoMaximo(r)
