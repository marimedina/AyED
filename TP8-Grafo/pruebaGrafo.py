from tdagrafo import *
import math
import random



# Eje 1 - Generar un grafo con 15 vertices aleatorios, luego agregue 30 aristas que
# conecten vertices de manera aleatoria.
'''
lv = listaAleatoriaVerticesSinRepetir(15)
g = Grafo()

for dato in lv:
    insertar_vertice(g, dato)

agregadas = 0
while agregadas < 30:
    origen = chr(random.randint(65, 90))
    destino = chr(random.randint(65, 90))
    insertar_arista(g, random.randint(1, 100), origen, destino)
    agregadas += 1
barrido_vertices(g)
'''

# Parte A - Primero eliminar los vertices que hayan quedado desconectados, es decir, que
# ningun otro vertice tenga una arista que lo apunte y que de el no salga ninguna
# arista.
'''
print('')
eliminados = eliminarVerticesDesconectados(g)
print('Informacion de nodos eliminados')
for nodo in eliminados:
    print(nodo.info)
'''

# Parte B - Determinar el nodo con mayor cantidad de aristas que salen de el, puede ser mas de uno
'''
print('')
print('Nodo con mayor salida de aristas:')
aux = cantidad_aristas_apuntando(g)
for elemento in aux:
    print(elemento.info)
'''

# Parte C - Determinar el nodo con mayor cantidad de aristas que llegan a el, puede ser mas de uno.
'''
print('')
print('Nodo con mayor entrada de aristas:')
aux = cant_aristas_entrada(g)
for elemento in aux:
    print(elemento.info)
'''

# Parte D - Indicar los vertices desde los cuales no se puede acceder a otro vertice.
'''
print('')
vertices_sin_salidas(g)
'''

# Parte E - Contar cuantos vertice componen el grafo, dado que se genera aleatoriamente y
# se eliminan los vertices que quedan desconcertados
'''
print('')
print('Cantidad de vertices:', g.tamanio)
'''

# Parte F - Determine cuantos vertices tiene un arista a si mismo, es decir, un ciclo directo
'''
print('Cantidad de vertices con una arista a si mismo')
aux = cant_vertices_ciclo(g)
'''

# Parte G - Determinar la arista mas larga, indicando su origen, destino y valor puede ser mas de una.
'''
aux = arista_mas_larga(g)
print('La arista mas larga es:')
for arista in aux:
    print("Origen: {}.  Destino: {}.  Distancia: {}". format(arista[0], arista[1], arista[2]))
'''

# -------------------------------------------------------------------------------------------------

# Ej 2 - Sobre el siguiente digrafo implemente los algoritmos necesarios para resolver las tareas
'''
g = Grafo(True)
vertices = ['A', 'B', 'C', 'D', 'E']

for elemento in vertices:
    insertar_vertice(g, elemento)

insertar_arista(g, random.randint(0,50), 'A', 'B')
insertar_arista(g, random.randint(0,50), 'B', 'C')
insertar_arista(g, random.randint(0,50), 'C', 'A')
insertar_arista(g, random.randint(0,50), 'A', 'C')
insertar_arista(g, random.randint(0,50), 'A', 'E')
insertar_arista(g, random.randint(0,50), 'C', 'D')
insertar_arista(g, random.randint(0,50), 'D', 'D')
barrido_vertices(g)
'''
# Parte A - Representarlo como arreglo de listas de adyacencias y lista de listas de adyacencia
'''
print('')
print('Arreglo de listas de adyacencias:')
mostrar_arreglo_ady(g)
print('Lista de listas de adyacencia:')
mostrar_lista_lista_ady(g)
'''

# Parte B - Cargue el valor de las etiquetas de todas las aristas
# Hecho al principio, al cargar el grafo.

# Parte C y D - Encuentre el arbol de expansion minima, para este punto considere el grafo como no dirigido.
# Agregue un arco de E hasta C
'''
#---- Cargo el mismo grafo pero no dirigido
print('')
g1 = Grafo(True)
vertices = ['A', 'B', 'C', 'D', 'E']

for elemento in vertices:
    insertar_vertice(g1, elemento)

insertar_arista(g1, random.randint(0,50), 'A', 'B')
insertar_arista(g1, random.randint(0,50), 'A', 'C')
insertar_arista(g1, random.randint(0,50), 'A', 'E')
insertar_arista(g1, random.randint(0,50), 'B', 'C')
insertar_arista(g1, random.randint(0,50), 'C', 'D')
insertar_arista(g1, random.randint(0,50), 'D', 'D')
barrido_vertices(g1)

print('Arbol de expansion minima:')
print(prim(g1))

print('')
insertar_arista(g1, random.randint(0,50), 'E', 'C')
barrido_vertices(g1)
'''

# Parte E - Encuentre el camino mas corto de A hasta D.
'''
print('')
aux = dijkstra(g, 'A', 'D')
print(aux)
'''


# -------------------------------------------------------------------------------------------------

# Ej 3 - Un empresa de telefonia celular dispone de la informacion de sus antenas, de las cuales se
#conoce: latitud y longitud, codigo de identificacion, velocidad de transferencia en
# megabytes/segundos, y ademas las antenas a las que transmite y las
#distancias a cada una de estas
'''
# Parte A y B
g = Grafo(False)
vertices = ('F', 'G', 'H', 'I', 'X', 'Y')
for elemento in vertices:
    insertar_objeto(g, antena_trasmite(elemento))

barrido_vertices(g)

c = 0
while c < 8:
    origen = random.choice(vertices)
    destino = random.choice(vertices)
    if origen != destino:
        insertar_arista(g, random.randint(0,50), origen, destino)
        c += 1
print('')
barrido_vertices(g)
'''

# Parte C - Determinar el tamanio
'''
print('El tamanio del grafo es:')
print(g.tamanio)
'''

# Parte D - Determinar el camino mas corto para transmitir desde la antena X a la antena Y,
# utilizando el algoritmo de Dijkstra
'''
aux = dijkstra(g, 'X', 'Y')
print('El camino mas corto es:')
print(aux)
'''

# Parte E - Encontrar el arbol de expansion minimo del grafo, utilizando Prim o Kruskal
'''
aux = Kruskal(g)
print('Arbol de expansion minima:')
print(aux)
'''

# Parte F - Determinar si la antena con codigo X existe, de ser asi mostrar toda su
#informacion.
'''
aux = buscar_vertice(g, 'X')
if aux:
    print('Datos de la antena')
    print(aux)
else:
    print('La antena X no fue encontrada')
'''


# -------------------------------------------------------------------------------------------------

# Ej 4 - Dado el esquema de red de la siguiente figura, cargarlo en un grafo e implementar los
#algoritmos necesarios para resolver las tareas
'''
g = Grafo(False)
tipo = ['pc', 'laptop', 'servidor', 'router', 'switch', 'impresora']

insertar_objeto(g, Red('Laptop-PT', 'Red Hat'))
insertar_objeto(g, Red('Server-PT', 'Guarani'))
insertar_objeto(g, Red('829', 'Router01'))
insertar_objeto(g, Red('829', 'Router02'))
insertar_objeto(g, Red('829', 'Router03'))
insertar_objeto(g, Red('Laptop-PT', 'Debian'))
insertar_objeto(g, Red('2960-27TT', 'Switch01'))
insertar_objeto(g, Red('PC-PT', 'Ubuntu'))
insertar_objeto(g, Red('Printer-PT', 'Printer'))
insertar_objeto(g, Red('PC-PT', 'Mint'))
insertar_objeto(g, Red('2960-24TT', 'Switch02'))
insertar_objeto(g, Red('PC-PT', 'Manjaro'))
insertar_objeto(g, Red('Server-PT', 'MongoDB'))
insertar_objeto(g, Red('PC-PT', 'Parrot'))
insertar_objeto(g, Red('PC-TP', 'Fedora'))
insertar_objeto(g, Red('Laptop-PT', 'Arch'))

insertar_arista(g, 25, 'Router02', 'Red Hat')
insertar_arista(g, 9, 'Router02', 'Guarani')
insertar_arista(g, 37, 'Router02', 'Router01')
insertar_arista(g, 50, 'Router02', 'Router03')
insertar_arista(g, 43, 'Router03', 'Router01')
insertar_arista(g, 29, 'Router01', 'Switch01')
insertar_arista(g, 17, 'Switch01', 'Debian')
insertar_arista(g, 18, 'Switch01', 'Ubuntu')
insertar_arista(g, 22, 'Switch01', 'Printer')
insertar_arista(g, 80, 'Switch01', 'Mint')
insertar_arista(g, 61, 'Router03', 'Switch02')
insertar_arista(g, 40, 'Switch02', 'Manjaro')
insertar_arista(g, 12, 'Switch02', 'MongoDB')
insertar_arista(g, 5, 'Switch02', 'Parrot')
insertar_arista(g, 56, 'Switch02', 'Fedora')
insertar_arista(g, 3, 'Switch02', 'Arch')
# barrido_vertices(g)
'''
# Parte B - Realizar un barrido en profundidad y amplitud partiendo desde la tres laptops:
# Red Hat, Debian, Arch
'''
print('Barrido en profundidad Red Hat:')
aux = buscar_vertice(g, 'Red Hat')
barrido_profundiad(g, aux)
'''
'''
print('Barrido en profundidad Debian:')
aux1 = buscar_vertice(g, 'Debian')
barrido_profundiad(g, aux1)
'''
'''
print('Barrido en profundidad Arch:')
aux2 = buscar_vertice(g, 'Arch')
barrido_profundiad(g, aux2)
'''
'''
print('Barrido en amplitud Red Hat:')
aux = buscar_vertice(g, 'Red Hat')
barrido_amplitud(g, aux)
'''
'''
print('Barrido en profundidad Debian:')
aux1 = buscar_vertice(g, 'Debian')
barrido_amplitud(g, aux1)
'''
'''
print('Barrido en profundidad Arch:')
aux2 = buscar_vertice(g, 'Arch')
barrido_amplitud(g, aux2)
'''

# Parte C - Encontrar el camino mas corto para enviar a imprimir un documentos desde la pc:
# Manjaro, Red Hat, Fedora hasta la impresora
'''
aux = dijkstra(g, 'Manjaro', 'Printer')
print(aux)
aux1 = dijkstra(g, 'Red Hat', 'Printer')
print(aux1)
aux2 = dijkstra(g, 'Fedora', 'Printer')
print(aux2)
'''

# Parte D - Encontrar el arbol de expansion minima
'''
aux = Kruskal(g)
print(aux)
'''

# Parte E - Determinar desde que pc (no laptop) es el camino mas corto hasta el servidor
# Guarani
'''
resultado = buscar_vertice(g, 'Guarani')
if resultado:
    largoDeCamCorto = math.isinf
    caminoCorto = []
    aux = g.inicio
    while aux is not None:
        if ('PC' in aux.tipo):
            camino, largo = dijkstra2(g, aux.info,'Guarani')
            if largo < largoDeCamCorto:
                largoDeCamCorto = largo
                caminoCorto = camino
        aux = aux.sig

    print('El camino mas corto desde una PC al servidor Guarani es:')
    print(caminoCorto)
'''

# Parte F - Indicar desde que computadora del switch 01 es el camino mas corto al servidor
# MongoDB
'''
switch = buscar_vertice(g, 'Switch01')
servidor = buscar_vertice(g, 'MongoDB')
if switch and servidor:
    lardoDelCamino = math.isinf
    caminoCorto = []
    aux = switch.adyacentes.inicio
    while aux is not None:
        resultado = buscar_vertice(g, aux.destino)
        if ('PC' in resultado.tipo) or ('Laptop' in resultado.tipo):
            camino, largo = dijkstra2(g, resultado.tipo, 'MongoDB')
            if largo < largoDelCamino:
                largoDelCamino = largo
                caminoCorto = camino
        aux = aux.sig
print('EL camino mas corto desde una computadora del switch 01 a Mongo es:')
print(caminoCorto)
'''

# Parte G - Cambie la conexion de la impresora al router 02 y vuelva a resolver el punto b
'''
aux = buscar_vertice(g, 'Printer')
eliminar_arista(g, aux, 'Switch01')
insertar_arista(g, 55, 'Printer', 'Switch02')

print('Barrido en profundidad Red Hat:')
aux = buscar_vertice(g, 'Red Hat')
barrido_profundiad(g, aux)

print('Barrido en profundidad Debian:')
aux1 = buscar_vertice(g, 'Debian')
barrido_profundiad(g, aux1)

print('Barrido en profundidad Arch:')
aux2 = buscar_vertice(g, 'Arch')
barrido_profundiad(g, aux2)

print('Barrido en amplitud Red Hat:')
aux3 = buscar_vertice(g, 'Red Hat')
barrido_amplitud(g, aux3)

print('Barrido en profundidad Debian:')
aux4 = buscar_vertice(g, 'Debian')
barrido_amplitud(g, aux4)

print('Barrido en profundidad Arch:')
aux5 = buscar_vertice(g, 'Arch')
barrido_amplitud(g, aux5)
'''





# Ej 6 - Implemente los algoritmos necesario para resolver las siguientes tareas sobre el grafo de la figura:
'''
g = Grafo(True)
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

for elemento in vertices:
    insertar_vertice(g, elemento)

insertar_arista(g, 15, 'A', 'B')
insertar_arista(g, 19, 'A', 'C')
insertar_arista(g, 13, 'A', 'D')
insertar_arista(g, 2, 'B', 'C')
insertar_arista(g, 12, 'B', 'F')
insertar_arista(g, 20, 'B', 'E')
insertar_arista(g, 5, 'C', 'E')
insertar_arista(g, 9, 'C', 'F')
insertar_arista(g, 27, 'C', 'G')
insertar_arista(g, 39, 'D', 'F')
insertar_arista(g, 45, 'D', 'G')
insertar_arista(g, 1, 'E', 'F')
insertar_arista(g, 3, 'F', 'G')
'''
# Parte A - Barrido en profundidad y amplitud partiendo de A, C, F
'''
aux = buscar_vertice(g, 'A')
barrido_amplitud(g, aux)
'''
'''
aux1 = buscar_vertice(g, 'C')
barrido_amplitud(g, aux1)
'''
'''
aux2 = buscar_vertice(g, 'F')
barrido_amplitud(g, aux2)
'''
'''
aux = buscar_vertice(g, 'A')
barrido_profundiad(g, aux)
'''
'''
aux1 = buscar_vertice(g, 'C')
barrido_profundiad(g, aux1)
'''
'''
aux2 = buscar_vertice(g, 'F')
barrido_profundiad(g, aux2)
'''
# Parte B - El camino mas corto de A hasta F, de C hasta D, de B hasta G
'''
aux = dijkstra(g, 'A', 'F')
print(aux)
'''
'''
aux = dijkstra(g, 'C', 'D')
print(aux)
'''
'''
aux2 = dijkstra(g, 'B', 'G')
print(aux2)
'''

# Parte C - Agrega una arista de C hasta A, de C hasta B, de G hasta D y vuelva a ejecutar los
# puntos del item anterior si camino
'''
insertar_arista(g, 11, 'C', 'A')
insertar_arista(g, 11, 'C', 'B')
insertar_arista(g, 11, 'G', 'D')

print(dijkstra(g, 'A', 'F'))
print(dijkstra(g, 'C', 'D'))
print(dijkstra(g, 'B', 'G'))
'''

# Parte D - Realice la representacion de matriz de adyacencia del grafo
'''
mostrar_arreglo_ady(g)
'''


# Ej 7 - Implementar un grafo social y los algoritmos necesarios para atender los requerimientos
'''
# Parte A - Cargar personas como vertices del grafo
g = Grafo(True)
cargar_persona(g)

# Parte B - Cargar aristas con las siguientes etiquetas: Twitter, Instagram, Facebook y la
# cantidad de retwitters y me gusta respectivamente, que representan si la persona
# del vertice origen sigue o es amigo de la persona del vertice destino

cargar_arista_persona(g)
barrido_vertices(g)
'''
# Parte C - Hallar el arbol de expansion maximo para cada red social considere el grafo como
# no dirigido para este punto
'''
g1 = Grafo(False)
cargar_persona(g1)
cargar_arista_persona(g1)
barrido_vertices(g1)
print('--------------------------')
print(kruskal_rs(g1, 'FB'))
print(kruskal_rs(g1, 'TW'))
print(kruskal_rs(g1, 'IG'))
'''
# Parte D - Determine si es posible conectar la persona X con la persona Y a traves de la red
# social Twitter
'''
print('--')
aux = buscar_vertice(g, 'X')
if existe_camino_RS(g, aux, 'Y', 'TW'):
    print('Existe paso')
else:
    print('No exite paso')
'''

# Parte F - Indique a todas las persona que sigue a travss de su red de Instagram la persona Y
'''
resultado = buscar_vertice(g, 'Y')
if resultado is not None:
    aux_ady = resultado.adyacentes.inicio
    print('Personas que se siguen a traves de IG')
    while aux_ady is not None:
        if aux_ady.info[0] == 'IG':
            print(aux_ady.destino)
        aux_ady = aux_ady.sig
'''


# Ej 9 - Genere un grafo no dirigido con planetas de SW y disenie algoritmos
# necesarios para resolver las actividades.

# Parte A y B - Planetas que deben estar y agrego 7 mas
'''
planetas = ['Alderaan', 'Endor', 'Dagobah', 'Hoth', 'Tatooine',
'Kamino', 'Naboo', 'Mustafar', 'Sacrif', 'Bespin', 'Yavin',
'Coruscant', 'Corellia', 'Ord Mantell', 'Kessel']

g = Grafo(False)
for planeta in planetas:
    insertar_vertice(g, planeta)

#barrido_vertices(g)

insertar_arista(g, random.randint(0,100), 'Alderaan', 'Endor')
insertar_arista(g, random.randint(0,100), 'Alderaan', 'Dagobah')
insertar_arista(g, random.randint(0,100), 'Alderaan', 'Hoth')
insertar_arista(g, random.randint(0,100), 'Alderaan', 'Tatooine')

insertar_arista(g, random.randint(0,100), 'Endor', 'Tatooine')
insertar_arista(g, random.randint(0,100), 'Endor', 'Kamino')
insertar_arista(g, random.randint(0,100), 'Endor', 'Dagobah')
insertar_arista(g, random.randint(0,100), 'Endor', 'Hoth')

insertar_arista(g, random.randint(0,100), 'Dagobah', 'Tatooine')
insertar_arista(g, random.randint(0,100), 'Dagobah', 'Hoth')
insertar_arista(g, random.randint(0,100), 'Dagobah', 'Kamino')
insertar_arista(g, random.randint(0,100), 'Dagobah', 'Naboo')

insertar_arista(g, random.randint(0,100), 'Hoth', 'Tatooine')
insertar_arista(g, random.randint(0,100), 'Hoth', 'Kamino')
insertar_arista(g, random.randint(0,100), 'Hoth', 'Naboo')
insertar_arista(g, random.randint(0,100), 'Hoth', 'Mustafar')

insertar_arista(g, random.randint(0,100), 'Tatooine', 'Kamino')
insertar_arista(g, random.randint(0,100), 'Tatooine', 'Naboo')
insertar_arista(g, random.randint(0,100), 'Tatooine', 'Mustafar')
insertar_arista(g, random.randint(0,100), 'Tatooine', 'Sacrif')

insertar_arista(g, random.randint(0,100), 'Kamino', 'Naboo')
insertar_arista(g, random.randint(0,100), 'Kamino', 'Mustafar')
insertar_arista(g, random.randint(0,100), 'Kamino', 'Sacrif')
insertar_arista(g, random.randint(0,100), 'Kamino', 'Bespin')

insertar_arista(g, random.randint(0,100), 'Naboo', 'Mustafar')
insertar_arista(g, random.randint(0,100), 'Naboo', 'Sacrif')
insertar_arista(g, random.randint(0,100), 'Naboo', 'Bespin')
insertar_arista(g, random.randint(0,100), 'Naboo', 'Yavin')

insertar_arista(g, random.randint(0,100), 'Mustafar', 'Sacrif')
insertar_arista(g, random.randint(0,100), 'Mustafar', 'Bespin')
insertar_arista(g, random.randint(0,100), 'Mustafar', 'Yavin')
insertar_arista(g, random.randint(0,100), 'Mustafar', 'Coruscant')

insertar_arista(g, random.randint(0,100), 'Sacrif', 'Bespin')
insertar_arista(g, random.randint(0,100), 'Sacrif', 'Yavin')
insertar_arista(g, random.randint(0,100), 'Sacrif', 'Coruscant')
insertar_arista(g, random.randint(0,100), 'Sacrif', 'Corellia')

insertar_arista(g, random.randint(0,100),'Bespin', 'Yavin')
insertar_arista(g, random.randint(0,100),'Bespin', 'Coruscant')
insertar_arista(g, random.randint(0,100),'Bespin', 'Corellia')
insertar_arista(g, random.randint(0,100),'Bespin', 'Ord Mantell')

barrido_vertices(g)
'''

# Parte C - Encuentre el arbol de expansion minima en cuanto a costos para recorrer todos
# los planetas
'''
print('--------------------')
print(Kruskal(g))
'''

# Parte D - Hallar el camino mas corto de Tatooine a Dagobah, Alderaan a Endor
# y de Hath a Tatooine
'''
print(dijkstra(g, 'Tatooine', 'Dagobah'))
print(dijkstra(g, 'Alderaan', 'Endor'))
print(dijkstra(g, 'Hoth', 'Tatooine'))
'''

# Parte E - Determinar todos los planetas a los que se puede llegar desde Tatooine
'''
print('')
print('Planetas a los que se puede llegar desde Tatooine')
aux = buscar_vertice(g, 'Tatooine')
if aux:
    barrido_adyacentes(aux)
'''


# Ej 10 - Implementar un grafo no dirigido para almacenar puntos turisticos de interes pais
'''
# Parte A y B
g = Grafo(False)
puntos = ['Atenas', 'Zues', 'Hera', 'Apolo', 'Poseidon', 'Artemisa',
'Teatro de Dionisio']

cargar_puntos(g, puntos)
cargar_aristas_puntos(g, puntos)
barrido_vertices(g)
'''

# Parte C - Hallar el arbol de expansion minimo partiendo de cualquiera de estos lugares
'''
print(Kruskal(g))
'''

# Parte D - Hallar el camino mas corto para ir desde el Partenon hasta el templo de Apolo en
# Delfos
'''
# Partenon = Atenas
print(dijkstra(g, 'Atenas', 'Apolo'))
'''
