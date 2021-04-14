from tdaarbol import NodoArbol, busqueda, eliminar, inorden, altura
from tdaarbol import postorden, preorden, insertar, reemplazar, act_altura
from tdaarbol import balancear, rot_doble, rot_simple
from tdaarbol import *
import random



# FALTA

# 3 - Indice de Summerville
# 6 - Indices/Directorios/Archivos/Knuth
# 9 - Numero de nodos en nivel

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


# Ej 5 - Dado un arbol con los nombre de los superheroes y villanos de la saga Marvel Cinematic Universe

# Parte A - En cada nodo del arbol se almacenara un campo booleano que indica si es un heroe o un villano
'''
r = None
heroes = ["Ironman ", "Spiderman ", "CapitanAmerica ", "Dr.Strange ",
        "Hulk", "BlackPanter "]
villanos = ["Thanos", "Loki", "Ultron", "Vulture"]


for i in range(7):
    r = insertar(r, [random.choice(heroes), True])
    r = insertar(r, [random.choice(villanos), False])
preorden(r)
'''
# Parte B - Mostar todos los superheroes que empiezan con C
'''
print('')
print('Villanos ordenados alfabeticamente:')
Villanos(r)
'''

# Parte C - Mostar todos los superheroes que empiezan con C
'''
print('')
print('Superheroes que comienzan con C:')
superheroesConC(r)
'''

# Parte D - Determinar cua|ntos superheroes hay el arbol
'''
print('')
print(cantidadSuperheroes(r))
'''

# Parte E - Doctor Strange en realidad esta mal cargado, utilice una busqueda por proximidad
# para encontrarlo en el arbol y modificar su nombre.
'''
b = 'Dr.Strange'
buscado = busqProxCampo(r, b, 0)
if buscado is not None:
    nombre = buscado.info[0]
    buscado.info[0] = "Doctor Strange"
else:
    print('El personaje no fue encontrado')

print('')
inorden(r)
'''

# Parte F - Listar los superheroes ordenados de manera descendente.
'''
print('Superheroes ordenamos alfabeticamente descendente')
inordenInvertido(r)
'''

# Parte G - Generar un bosque a partir de este arbol, un arbol debe contener a los
# superheroes y otro a los villanos.
'''
print('')
bosque = [None, None]
ArmarBosque(r, bosque)

#Corroboro que armo ambos arboles
#inorden(bosque[0])
#inorden(bosque[1])

# i
print('Cantidad de nodos en el bosque de los heroes')
print(peso(bosque[0]))
print('Cantidad de nodos en el bosque de los villanos')
print(peso(bosque[1]))

# ii
print('')
print('Heroes ordenados alfabeticamente:')
inorden(bosque[0])
print('Villanos ordenados alfabeticamente:')
inorden(bosque[1])
'''



# Ej 7 - Desarrollar un algoritmo que implemente dos funciones, una para obtener el minimo nodo
# del arbol y la segunda para obtener el maximo.
'''
r = None
for i in range(0, 6):
    r = insertar(r, random.randint(0, 100))
inorden(r)

print('')
print('El nodo maximo es:')
print(nodoMaximo(r).info)
print('El nodo minimo es:')
print(nodoMinimo(r).info)
'''



# Ej 8 - desarrollar un algoritmo que permita comprimir los mensaje para
# enviarlo mas rapidos y no puedan ser interceptado
'''
tabla = [
        [0.2, "A"],
        [0.17, "F"],
        [0.13, "1"],
        [0.21, "3"],
        [0.05, "0"],
        [0.09, "M"],
        [0.15, "T"]
    ]

# Parte A - Crear un arbol de Huffman a partir de la tabla
r = arbolHuffman(tabla)
imprimir(r)

# Parte B - Desarrollar las funcionas para comprimir y descomprimir un mensaje
print('')
msj = 'AF130MT'
msj_comprimido = comprimir(r, msj)
print('Mensaje comprimido: ', msj_comprimido)
msj_descomprimido = descomprimir(r, msj_comprimido)
print('Mensaje descomprimido: ', msj_descomprimido)
'''



# Ej 9 -
'''
r = None
for i in range(0, 6):
    r = insertar(r, random.randint(0, 100))
inorden(r)

for i in range(altura(r)):
    cant = nodosPorNivel(r, i,)
    aux = cantNodosCompletarNivel(r)
    if cant == aux:
        print('El nivel' + i + 'esta completo')
    else:
        print('Para completar este nivel, faltan' + aux + 'nodos')
'''


# Ej 10 - Escribir un algoritmo que permita resolver las siguientes actividades:
'''
r = None
for i in range(0, 6):
    r = insertar(r, random.randint(0, 100))
preorden(r)
'''

# Parte A - Contar el numero de nodos del arbol
'''
print('')
print('Cantidad de nodos del arbol:')
print(cantNodosArbol(r))
'''

# Parte B - Determinar el numero de hojas del arbol
'''
print('')
print('Cantidad de hojas del arbol')
print(cantHojasArbol(r))
'''

# Parte C - Mostrar la informacion de los nodos hojas
'''
print('')
print('Informacion de las hojas del arbol')
print(mostrarHojas(r))
'''

# Parte D - Determinar el padre de un nodo
'''
print('')
busc = 25
padre = obtenerPadre(r, busc)
if padre != busc:
    if padre is not None:
        print('El padre de ' + str(busc) + ' es ' + str(padre.info))
    else:
        print('No se encontro a ' + str(busc))
else:
    print(str(busc) + ' es raiz')
'''

# Parte E - Determinar la altura de un arbol
'''
print('')
print('La altura del arbol es :' + str(r.altura))
'''


# Ej 11
