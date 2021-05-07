from tdaarbol import NodoArbol, busqueda, eliminar, inorden, altura
from tdaarbol import postorden, preorden, insertar, reemplazar, act_altura
from tdaarbol import balancear, rot_doble, rot_simple
from tdaarbol import *
import random



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


# Ej 3 - Desarrollar un algoritmo que permita cargar el indice del libro Ingenieria de Software de
# Ian Summerville de manera automatica desde un archivo de texto, transformando el arbol
# n-ario del indice en un arbol binario no balanceado mediante el uso de la transformada deKnuth

'''
txtToDat("IndicesSummerville/indice_summerville.txt", "IndicesSummerville/indice_summerville")

a_indices = abrir("Indices/indice_summerville")
arbol_nario = fileToNario(a_indices)
cerrar(a_indices)
arbol_b = transformarKnuth(arbol_nario)
'''
# Parte A - Listar el indice en su orden original
'''
barridoKnuth(arbol_b)
'''

# Parte B - Mostrar la parte del indice correspondiente al subtitulo Disenio de software de tiempo real
'''
mostrarParte(arbol_b, '15. Disenio de software de tiempo real 309')
'''

# Parte D - Determinar cuantos capitulos tiene
'''
cantidad_capitulos = contarCantidadCapitulos(arbol_b)
print(cantidad_capitulos)
'''

# Parte E - Determinar todos los temas que contengan las palabras modelo y metrica
'''
lista_coincidencias = []
buscados = ["modelo", "metrica"]
for buscado in buscados:
    busquedaCoincidenciasKnuth(arbol_b, buscado, lista_coincidencias)
if len(lista_coincidencias) > 0:
    for nodo_coincidente in lista_coincidencias:
        print(nodo_coincidente.info)
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



# Ej 9 - Desarrollar dos algoritmos el primero que permita calcular en el numero de nodos de un
# nivel del arbol  y la segunda que cuente los nodos que hay en dicho nivel
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


# Ej 14 - Desarrollar un algoritmo que permita implementar un arbol como indice para hacer
# consultas a un archivo, el cual contiene personajes de la saga de Star Wars de los cuales se
# sabe su nombre, altura y peso
'''
ruta = 'SW/personajesStarWars'
arbol_nombres = generarArbolPersonajesNombre(ruta)
'''

# Parte B - Se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos)
# y darlo de baja
'''
arbol_nombres = altaPersonaje(arbol_nombres, ruta)
arbol_nombres = modificarPersonaje(arbol_nombres, ruta)
arbol_nombres = bajaPeronsaje(arbol_nombres, ruta)
'''

# Parte C - Mostrar toda la informacion de Yoda y Boba Fett
'''
consultaPersonaje(arbol_nombres, "Yoda", ruta)
consultaPersonaje(arbol_nombres, "Boba Fett", ruta)
'''

# Parte D - Mostrar un listado ordenado alfabeticamente de los personajes que miden mas de
# 1 metro.
'''
archivo = abrir(ruta)
listadoIndicesAltura(arbol_nombres, archivo)
'''

# Parte E - Mostrar un listado ordenado alfabeticamente de los personajes que pesan menos
# de 75 kilos.
'''
listadoIndicesPeso(arbol_nombres, archivo)
'''


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


# Ej 17 - La armeria de la base Starkiller, central de la primera orden, almacena los registros de los
# reportes de fallos armas de las tropas de su principales generales Kylo Ren, general Hux y
# capitana Phasma para lo cual se solicita desarrollar un algoritmo

# Parte A - Se debe registrar el nombre del general a cargo de la mision, fecha de la mision,
# codigo de blaster generado de manera aleatoria, estado del blaster (si fallo o no) y el
# tipo de soldado que portaba el blaster Imperial Stromtrooper, Imperial Scout Trooper,
# Imperial Death Trooper, Sith Trooper y First Order Stromtrooper.

'''funcion realizada en TDA'''

# Parte B - Debe generar y cargar al menos 10000 registros.
'''
# cambiar range(10) por 10.000
arbol = None
for i in range(10):
    reg = generarRegistro(i)
    arbol = insertarCampo(arbol, reg, 0)
preorden(arbol)
'''

# Parte C - Determinar el total de armas que fallaron por general.
'''
print('')
armasFalladas(arbol)
'''

# Parte D - Indicar la cantidad y tipo de soldado de las misiones de Kylo Ren
'''
print('')
cantSoldados(arbol, 'Kylo Ren')
'''

# Parte E - Determinar cuantos Sith Troopers salieron en misiones y a cuantos les fallaron los blasters
'''
print('')
Sith_Fallas(arbol)
'''

# Parte F - Listar los codigos de los blasters de las misiones de una determinada fecha,
# indicando ademas el porcentaje de armas que fallaron.
'''
print('')
codMision(arbol, '01/01/2001')
'''



# Ej 18 - Desarrollar los algoritmo necesarios que permitan almacenar libros de los cuales se
# conoce su titulo, ISBN, autores, editorial y cantidad paginas
'''
ruta_file = 'Libros/libros'
initFileLibros()
a_Titulo = generarArbolLibro(ruta_file, 'titulo')
a_ISBN = generarArbolLibro(ruta_file, 'isbn')
a_Autores = generarArbolLibro(ruta_file, 'autores')

imprimir(a_Titulo)
print('')
imprimir(a_Autores)
print('')
imprimir(a_ISBN)
'''

# Parte A - Los libros de los autores Tanenbaum, Connolly, Rowling, Riordan
'''
libros_tanenbaum = busquedaPorAutor(arbolAutores, "Tanenbaum")
libros_connolly = busquedaPorAutor(arbolAutores, "Connolly")
libros_rowling = busquedaPorAutor(arbolAutores, "Rowling")
libros_roirdan = busquedaPorAutor(arbolAutores, "Roirdan")

libros = libros_tanenbaum + libros_connolly + libros_rowling + libros_roirdan

indices = set()
for libro in libros:
    indices.add(libro[1])

archivo = abrir(ruta_file)
libros_deseados = leerIndices(archivo, indices)
cerrar(archivo)

for libro in libros_deseados:
    print(libro)
'''

# Parte B - Mostrar los libros de Mineria de Datos, Algoritmos y Bases de Datos
'''
libros_mineria = busquedaPorCoincidenciaTitulo(arbolTitulo, "Mineria de Datos")
libros_algoritmos = busquedaPorCoincidenciaTitulo(arbolTitulo, "Algoritmos")
libros_bbdd = busquedaPorCoincidenciaTitulo(arbolTitulo, "Base de Datos")

libros = libros_mineria + libros_algoritmos + libros_bbdd

indices = set()
for libro in libros:
    indices.add(libro[1])

archivo = abrir(ruta_file)
libros_deseados = leerIndices(archivo, indices)
cerrar(archivo)

for libro in libros_deseados:
    print(libro)
'''

# Parte C - Mostrar los libros de mss de 873 paginas
'''
arbolPaginas = generarArbolLibro(ruta_file, "paginas")
paginas_deseadas = 873
indices_a_buscar = []
busqPag(arbolPaginas, paginas_deseadas, indices_a_buscar)

libros = []
archivo = abrir(ruta_file)
for indice in indices_a_buscar:
    libros.append(leer(archivo, indice))
cerrar(archivo)

for libro in libros:
    print(libro)
'''

# Parte D - Mostrar los datos del libro ISBN 9788420546391
'''
isbn_buscado = 9788420546391

nuevo_libro = Libro("PuntoD", isbn_buscado, ["autorRandom"], "edit2", 203)
archivo = abrir(ruta_file)
guardar(archivo, nuevo_libro)
cerrar(archivo)
arbolTitulo = generarArbolLibro(ruta_file, "titulo")
arbolISBN = generarArbolLibro(ruta_file, "isbn")
arbolAutores = generarArbolLibro(ruta_file, "autores")

res = busquedaPorISBN(arbolISBN, isbn_buscado)
if res:
    indice = res[1]
    archivo = abrir(ruta_file)
    libro = leer(archivo, indice)
    cerrar(archivo)
    print(libro)
'''

# Ej 19 - Implementar un algoritmo que permita generar un arbol de decision meteorologico para
# la prediccion del estado del tiempo basado reglas.
'''
Ar_reg = genArbolMeteorologico()
reg = genRegistroMeteorologico()
print("Registro analizado:", reg)
pronostico = definirPronostico(Ar_reg, reg)
print('Pronostico:', pronostico)
'''

# Ej 21 - Implementar un algoritmo que permita generar un arbol con los datos de la siguiente
# tabla y resuelva
'''
criaturaDerrotado = [
            ['Ceto', '', ''],
            ['Tifon', 'Zeus', ''],
            ['Equidna', 'Argos Panoptes', ''],
            ['Dino', '', ''],
            ['Pefredo', '', ''],
            ['Enio', '', ''],
            ['Escila', '', ''],
            ['Caribdis', '', ''],
            ['Euriale', '', ''],
            ['Esteno', '', ''],
            ['Medusa', 'Perseo', ''],
            ['Ladon', 'Heracles', ''],
            ['Aguila del Caucaso', '', ''],
            ['Quimera', 'Belerofonte', ''],
            ['Hidra de Lerna', 'Heracles', ''],
            ['Leon de Nemea', 'Heracles', ''],
            ['Esfinge', 'Edipo', ''],
            ['Dragon de la Colquida', '', ''],
            ['Cerbero', '', ''],
            ['Cerda de Cromion', 'Teseo', ''],
            ['Ortro', 'Heracles', ''],
            ['Toro de Creta', 'Teseo', ''],
            ['Jabali de Calidon', 'Atalanta', ''],
            ['Carcinos ', '', ''],
            ['Gerion', 'Heracles', ''],
            ['Cloto', '', ''],
            ['Laquesis', '', ''],
            ['Atropos', '', ''],
            ['Minotauro de Creta', 'Teseo', ''],
            ['Harpias', '', ''],
            ['Argos Panoptes', 'Hermes', ''],
            ['Aves del Estinfalo', '', ''],
            ['Talos', 'Medea', ''],
            ['Sirenas', '', ''],
            ['Piton', 'Apolo', ''],
            ['Cierva de Cerinea', '', ''],
            ['Basilisco', '', ''],
            ['Jabali de Erimanto', '', '']
        ]
arbolC = None
for criatura in criaturaDerrotado:
    arbolC = insertarCampo(arbolC, criatura, 0)
'''
# Parte A - Listado inorden de las criaturas y quienes la derrotaron
'''
inorden(arbolC)
'''

# Parte B - Se debe permitir cargar una breve descripcion sobre cada criatura
'''
criatura = 'Tifon'
aux = busquedaCampo(arbolC, criatura, 0)
if aux is not None:
    agregarDescripcion(arbolC, criatura, 'Criatura x')
    print("Nombre:", aux.info[0])
    print("Derrotado por:", aux.info[1])
    print("Descripcion:", aux.info[2])
'''

# Parte C - Mostrar toda la informacion de la criatura Talos
'''
criatura = 'Talos'
aux = busquedaCampo(arbolC, criatura, 0)
print('Nombre:', aux.info[0])
print('Derrotado por:', aux.info[1])
print('Descripcion:', aux.info[2])
'''

# Parte D - Determinar los 3 heroes o dioses que derrotaron mayor cantidad de criaturas
'''
lista_vencedores = vencedores(arbolC)
vencedores = sorted(lista_vencedores, key=lambda x: lista_vencedores.count(x), reverse=True)
mayores_vencedores = eliminarDuplicados(vencedores)

print('Mayores 3 vencedores:')
for i in range(3):
    print(mayores_vencedores[i])
'''

# Parte E - Listar las criaturas derrotadas por Heracles
'''
nombre = 'Heracles'
heroes = []
criaturasDerrotadasPor(arbolC, nombre, heroes)
print('Criaturas derrotadas por Heracles:')
for criatura in heroes:
    print(criatura[0])
'''

# Parte F - Listar las criaturas que no han sido derrotadas
'''
aux = []
criaturasDerrotadasPor(arbolC, '', aux)
print('Criaturas que nunca fueron derrotadas:')
for criatura in aux:
    print(criatura[0])
'''

# Parte G - Se debe permitir busquedas por coincidencia
'''
nombre = 'Ce'
encontradas = []
busquedaProximidadCriatura(arbolC, nombre, encontradas)
for criatura in encontradas:
    print(criatura[0])
'''

# Parte H - Eliminar al Basilisco y a las Sirenas
'''
nom1 = 'Basilisco'
nom2 = 'Sirenas'
eliminarCampo(arbolC, nom1, 0)
eliminarCampo(arbolC, nom2, 0)
print('Arbol sin Basilisco y Sirenas')
inorden(arbolC)
'''

# Parte I - Modificar el nodo que contiene a las Aves del Estinfalo, agregando que Heracles
# derroto a varias
'''
nombre = 'Aves del Estinfalo'
modificarDerrotadoPor(arbolC, nombre , 'Heracles')
'''

# Parte J - Modifique el nombre de la criatura Ladon por Dragon Ladon
'''
nomre_act = 'Ladon'
nombre_nuevo = 'Dragon Ladon'
modificarnombreCriatura(arbolC, nomre_act, nombre_nuevo)
inorden(arbolC)
'''


# Ej 22 - Desarrollar los algoritmos necesarios para generar un arbol de Huffman a partir de la
# siguiente tabla para lo cual debera calcular primero las frecuencias de cada caracter a
# partir de la cantidad de apariciones del mismo
'''
tabla = [
    ["A", 11, 0],
    ["B", 2, 0],
    ["C", 4, 0],
    ["D", 3, 0],
    ["E", 14, 0],
    ["G", 3, 0],
    ["I", 6, 0],
    ["L", 6, 0],
    ["M", 3, 0],
    ["N", 6, 0],
    ["O", 7, 0],
    ["P", 4, 0],
    ["Q", 1, 0],
    ["R", 10, 0],
    ["S", 4, 0],
    ["T", 3, 0],
    ["U", 4, 0],
    ["V", 2, 0],
    [" ", 17, 0],
    [",", 2, 0]
]

asignarFrecuencias(tabla)
tabla_para_huffman = formatearTablaParaHuffman(tabla)
arbol_huffman = arbolHuffman(tabla_para_huffman)
'''
# Parte B - Descomprimir los siguientes mensajes
'''
mensaje1 = '10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100'
mensaje2 = '0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010'

msj1 = descomprimir2(arbol_huffman, mensaje1)
print(msj1)
msj2 = descomprimir2(arbol_huffman, mensaje2)
print(msj2)
'''
