from tdaarbol import NodoArbol, busqueda, eliminar, inorden, altura
from tdaarbol import postorden, preorden, insertar, reemplazar, act_altura
from tdaarbol import balancear, rot_doble, rot_simple
from tdaarbol import *
import random



# FALTA

# 3 - Indice de Summerville
# 6 - Indices/Directorios/Archivos/Knuth
# 9 - Numero de nodos en nivel

# 14 - Consulta a archivos NH
# 16 - Pokemons NH

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


# Ej 11 - Generar un arbol binario que tenga nueve niveles, luego disenar los algoritmos necesarios
# para resolver las siguientes actividades:
'''
r = arbolDeXNiveles(5)
preorden(r)
print('')


# Parte A - Generar un bosque cortando los tres primeros niveles del arbol

print('')
bosque = []
recortarArbol(r, bosque, 3)

for arbol in bosque:
    print("---------------------")
    imprimir(arbol)
'''

# Parte B - Contar cuantos nodos tiene cada arbol del bosque
'''
for arbol in bosque:
    print('')
    print('Raiz:', arbol.info, ' Cantidad de nodos: ', peso(arbol))
'''

# Parte C - Realizar un barrido preorden de cada arbol del bosque
'''
for i in range(len(bosque)):
    print('')
    print("Barrido arbol " + str(i+1))
    preorden(bosque[i])
'''

# Parte D - Determinar cual es el arbol con mayor cantidad de nodos
'''
if len(bosque) == 0:
    print('Bosque vacio')
else:
    mayor = bosque[0]
    cant = peso(mayor)
    for arbol in bosque:
        if cant <= peso(arbol):
            mayor = arbol
            cant = peso(arbol)
print('')
print('El arbol con mayor cantidad de nodos es el de raiz ', mayor.info, ' con ', cant, ' nodos')
'''

# Parte E - Indicar que arboles del bosque estan llenos
'''
for arbol in bosque:
    if arbolLleno(arbol):
        print('El arbol cuya raiz es ', arbol.info, ' esta lleno')
    else:
        print('El arbol cuya raiz es ', arbol.info, ' no esta lleno')
'''


# Ej 12 - Nick Fury lider de la agencia S.H.I.E.L.D. tiene la dificil tarea de decidir que vengador
# asignara a cada nueva mision por lo que nos solicita desarrollar un arbol de decision para resolver esta
# tarea
'''
superheroes = ['Guardianes de las galaxias','Ant-Man','Hulk','Capitan America',
                'Capitana Marvel','Spiderman','Black Widow','Iron Man', 'Dr. Strange',
                'Thor']

asignacion = [
    {'mision': 'Intergalactica', 'peso': 1000, 'asignado': ["Guardianes de las galaxias", "Capitana Marvel"]},
    {'mision': 'En equipo', 'peso': 2000, 'asignado': ["Guardinaes de las galaxias"]},
    {'mision': 'Recuperacion', 'peso': 3000, 'asignado': ["Ant-Man", "Capitan America", "Black Widow"]},
    {'mision': 'Destruccion', 'peso': 4000, 'asignado': ["Hulk", "Thor"]},
    {'mision': 'Defensa', 'peso': 5000, 'asignado': ["Capitan America", "Spiderman", "Iron Man"]},
    {'mision': 'Poderoso', 'peso': 6000, 'asignado': ["Capitana Marbel", "Thor"]},
    {'mision': 'Estretegica', 'peso': 7000, 'asignado': ["Iron Man", "Dr. Strange"]}
]

arbolDec = arbolDecision(asignacion)
print('Los heroes asignados para la mision Intergalactica son:')
heroes = asignarHeroe('Intergalactica', arbolDec)
if heroes:
    print(heroes)
'''


# Ej 13 - Desarrollar un algoritmo que permita decodificar mensajes en codigo morse.
'''
l_morse = [ ['E', 850000],
                ['T', 2450000],
                ['I', 450000],
                ['A', 1250000],
                ['N', 2050000],
                ['M', 2850000],
                ['S', 250000],
                ['U', 650000],
                ['R', 1050000],
                ['W', 1450000],
                ['D', 1850000],
                ['K', 2250000],
                ['G', 2650000],
                ['O', 3050000],
                ['H', 150000],
                ['V', 350000],
                ['F', 550000],
                [' ', 750000],
                ['L', 950000],
                [' ', 1150000],
                ['P', 1350000],
                ['J', 1550000],
                ['B', 1750000],
                ['X', 1950000],
                ['C', 2150000],
                ['Y', 2350000],
                ['Z', 2550000],
                ['Q', 2750000],
                [' ', 2950000],
                [' ', 3150000],
                ['5', 100000],
                ['4', 200000],
                [' ', 300000],
                ['3', 400000],
                [' ', 500000],
                [' ', 600000],
                [' ', 700000],
                ['2', 800000],
                [' ', 900000],
                [' ', 1000000],
                [' ', 1100000],
                [' ', 1200000],
                [' ', 1300000],
                [' ', 1400000],
                [' ', 1500000],
                ['1', 1600000],
                ['6', 1700000],
                [' ', 1800000],
                [' ', 1900000],
                [' ', 2000000],
                [' ', 2100000],
                [' ', 2200000],
                [' ', 2300000],
                [' ', 2400000],
                ['7', 2500000],
                [' ', 2600000],
                [' ', 2700000],
                [' ', 2800000],
                ['8', 2900000],
                [' ', 3000000],
                ['9', 3100000],
                ['0', 3200000]
            ]

msj1 = '.--. .- ... . / .-.. --- / --.- ..- . / .--. .- ... . / -- .- .- -. .- / .--. .-. --- -- . - . -- . / .- .-.. --. --- /--.- ..- . / ...- .- / ... . --. ..- .. .-. / ... .. . -. -.. --- / ..- ... - . -.. / -. --- / ..- -. / ... --- .-.. -.. .- -.. --- / .--. . .-. ..-. . -.-. - --- / ... .. -. --- / ..- -. / -... ..- . -. /.... --- -- -... .-. . .-.-.'
msj2 = '-. --- ... --- - .-. --- ... / ... --- -- --- ... / .-.. --- ... / -- .- .-.. -.. .. - --- ... / --. ..- .- .-. -.. .. .- -. . ... / -.. . / .-.. .- / --. .- .-.. .- -..- .. .- .-.-.'
msj3 = '-.-- --- / ... --- .-.. --- / .- -.-. - ..- --- / -.-. --- -- --- / ... .. / . -. / ...- . .-. -.. .- -.. / .-.. --- / ... ..- .--. .. . .-. .- / - --- -.. --- .-.-.'
msj4 = '-.-. .... .. -.-. --- ... / . ... - --- -.-- / .-.. .-.. . ...- .- -. -.. --- / .-.. .- / ..-. .. . ... - .- / .... .- -.-. .. .- / ..- ... - . -.. . ... .-.-.'
msj5 = '.--. --- -.. .-. .. .- / .... .-  -.-. . .-. / . ... - --- / - --- -.. --- / . .-.. / -.. .. .- .-.-.'

a = arbolMorse(l_morse)

print('Mensaje 1:')
print(decodificarMsj(a, msj1))
print('Mensaje 2:')
print(decodificarMsj(a, msj2))
print('Mensaje 3:')
print(decodificarMsj(a, msj3))
print('Mensaje 4:')
print(decodificarMsj(a, msj4))
print('Mensaje 5:')
print(decodificarMsj(a, msj5))
'''


# Ej 14 -



# Ej 15 - Una empresa de nano satelites dedicada al monitoreo de lotes campo destinados al agro,
# tiene problemas para la transmision de los datos recolectados, dado que la ventana de
# tiempo que dispone para enviar los datos antes de una nueva medicion es muy corta, por
# lo que nos solicita desarrollar un algoritmo que permita comprimir la informacion para
# poder enviarla mas rapida.
'''
tabla = [
            [0.22, "Despejado"], [0.15, "Nublado"], [0.03, "Lluvia"],
            [0.26, "Baja"], [0.14, "Alta"], [0.05, "1"], [0.01, "2"],
            [0.035, "3"], [0.06, "5"], [0.02, "7"], [0.025, "8"]
        ]
# Parte B - Desarrollar un arbol de Huffman que permita comprimir la informacion para transmitirla
r = arbolHuffman(tabla)

# Parte C - Comprimir un mensaje y descomprimirlo
msj_original = nanoMensaje()
print(msj_original)
print('Mensaje comprimido:')
msj_comprimido = comprimirMed(r, msj_original)
print(msj_comprimido)
print('Mensaje descomprimido:')
msj_descomprimido = descomprimirMed(r, msj_comprimido)
print(msj_descomprimido)
'''


# Ej 17 -

# Parte A - Se debe registrar el nombre del general a cargo de la mision, fecha de la mision,
# codigo de blaster generado de manera aleatoria, estado del blaster (si fallo o no) y el
# tipo de soldado que portaba el blaster Imperial Stromtrooper, Imperial Scout Trooper,
# Imperial Death Trooper, Sith Trooper y First Order Stromtrooper.

'''funcion realizada en TDA'''

# Parte B - Debe generar y cargar al menos 10000 registros.

'''cambiar range(10) por 10.000'''
arbol = None
for i in range(10):
    reg = generarRegistro(i)
    arbol = insertarCampo(arbol, reg, 0)
preorden(arbol)

# Parte C - Determinar el total de armas que fallaron por general.
print('')
armasFalladas(arbol)
