from tdapila import apilar, desapilar, barrido, pila_vacia, invertir, copiarPila, Pila
from tdacola import Cola, arribo, atencion, cola_vacia
from tdaheap import Heap, arribo_H, atencion_H, heap_vacio, cambiarPrioridad
from tdaheap import barridoMonticulo, buscar_H
import random
from math import isinf

class Grafo():
    inicio, tamanio = None, 0

    def __init__(self, dirigido=True):
        self.inicio = None
        self.tamanio = 0
        self.dirigido = dirigido

class Vertice():
    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = lista_arista()


class Arista():
    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.sig = None


class lista_arista():
    def __init__(self, dirigido=True):
        self.inicio = None
        self.tamanio = 0


def insertar_vertice(grafo, dato):
    nodo = Vertice(dato)
    nodo.info = dato
    if grafo.inicio is None or nodo.info < grafo.inicio.info:
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        act = grafo.inicio.sig
        ant = grafo.inicio
        while (act is not None) and (act.info <= nodo.info):
            act = act.sig
            ant = ant.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1


def agregar_arista(lista_adyacentes, dato, destino):
    nodo = Arista(dato, destino)
    if (lista_adyacentes.inicio is None) or (destino < lista_adyacentes.inicio.destino):
        nodo.sig = lista_adyacentes.inicio
        lista_adyacentes.inicio = nodo
    else:
        ant = lista_adyacentes.inicio
        act = lista_adyacentes.inicio.sig

        while(act is not None and act.destino < nodo.destino):
            ant = act
            act = act.sig

        nodo.sig = act
        ant.sig = nodo

    lista_adyacentes.tamanio += 1


def insertar_arista(grafo, dato, origen, destino):
    origen = buscar_vertice(grafo, origen)
    destino = buscar_vertice(grafo, destino)
    if (origen is not None) and (destino is not None):
        if grafo.dirigido:
            agregar_arista(origen.adyacentes, dato, destino.info)
        else:
            agregar_arista(origen.adyacentes, dato, destino.info)
            agregar_arista(destino.adyacentes, dato, origen.info)


def buscar_arista(vertice, buscado):
    aux = vertice.adyacentes.inicio
    while (aux is not None) and (aux.destino != buscado):
        aux = aux.sig
    return aux


def buscar_vertice(grafo, buscado):
    aux = grafo.inicio
    while (aux is not None) and (aux.info != buscado):
        aux = aux.sig
    return aux


def barrido_profundiad(grafo, vertice):
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio
            while adyacentes is not None:
                aux_adyacente = buscar_vertice(grafo, adyacentes.destino)
                if not aux_adyacente.visitado:
                    barrido_profundiad(grafo, aux_adyacente)
                adyacentes = adyacentes.sig
        vertice = vertice.sig


def barrido_amplitud(grafo, vertice):
    cola = Cola()
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            arribo(cola, vertice)
            while not cola_vacia(cola):
                nodo = atencion(cola)
                print(nodo.info)
                aux_adyacentes = nodo.adyacentes.inicio
                while aux_adyacentes is not None:
                    resultado = buscar_vertice(grafo, aux_adyacentes.destino)
                    if not resultado.visitado:
                        resultado.visitado = True
                        arribo(cola, resultado)
                    aux_adyacentes = aux_adyacentes.sig
        vertice = vertice.sig


def barrido_vertices(grafo):
    aux = grafo.inicio
    while aux is not None:
        print("Vertice:", aux.info)
        print("Adyacentes:")
        barrido_adyacentes(aux)
        aux = aux.sig
        print()


def barrido_adyacentes(vertice):
    aux = vertice.adyacentes.inicio
    while(aux is not None):
        print("Destino: {}  -   Info: {}".format(aux.destino, aux.info))
        aux = aux.sig


def grafo_vacio(grafo):
    return grafo.inicio is None


def existe_paso(grafo, origen, destino):
    resultado = False
    if not origen.visitado:
        origen.visitado = True
        vadyacentes = origen.adyacentes.inicio
        while vadyacentes is not None and not resultado:
            adyacente = buscar_vertice(grafo, vadyacentes.destino)
            if adyacente.info == destino.info:
                return True
            elif not adyacente.visitado:
                resultado = existe_paso(grafo, adyacente, destino)
            vadyacentes = vadyacentes.sig
    return resultado


def marcar_no_visitado(grafo):
    aux = grafo.inicio
    while aux is not None:
        aux.visitado = False
    aux = aux.sig


def eliminar_vertice(grafo, clave):
    dato = None
    if grafo.inicio.info == clave:
        dato = grafo.inicio.info
        grafo.inicio = grafo.inicio.sig
        grafo.tamanio -= 1
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while (act is not None) and (act.info != clave):
            ant = act
            act = act.sig
        if (act is not None):
            dato = act.info
            ant.sig = act.sig
            grafo.tamanio -= 1
    if(dato is not None):
        aux = grafo.inicio
        while aux is not None:
            if aux.adyacentes.inicio is not None:
                quitar_arista(aux, dato)

    return dato


def quitar_arista(vertice, destino):
    info_extraida = None
    aux_adyacentes = vertice.adyacentes.inicio

    if aux_adyacentes.destino == destino:
        info_extraida = aux_adyacentes.info
        vertice.adyacentes.inicio = aux_adyacentes.sig
        vertice.adyacentes.tamanio -= 1
    else:
        ant = aux_adyacentes
        act = aux_adyacentes.sig

        while (act is not None) and (act.destino != destino):
            ant = act
            act = act.sig

        if (act is not None):
            info_extraida = act.info
            ant.sig = act.sig
            vertice.adyacentes.tamanio -= 1

    return info_extraida


def eliminar_arista(grafo, vertice, destino):
    nodo_quitado = quitar_arista(vertice, destino)
    if not grafo.dirigido:
        nodo_origen = buscar_vertice(grafo, destino)
        quitar_arista(nodo_origen, vertice.info)
    return nodo_quitado



# para insertar
'''origen = buscar_vertice(grafo, 'A')
destino = buscar_arista(origen, )
if origen is not None and destino si not None:
    insertar_arista(grafo, 20, origen, destino)'''


def Kruskal(grafo):
    bosque = []
    heap_aristas = Heap(grafo.tamanio**2)
    aux_vertices = grafo.inicio

    while aux_vertices is not None:
        bosque.append([aux_vertices.info])
        adyacentes = aux_vertices.adyacentes.inicio

        while adyacentes is not None:
            datos = [aux_vertices.info, adyacentes.destino]
            peso = adyacentes.info
            arribo_H(heap_aristas, peso, datos)
            adyacentes = adyacentes.sig
        aux_vertices = aux_vertices.sig

    while (len(bosque) > 1) and (not heap_vacio(heap_aristas)):
        datos_y_peso = atencion_H(heap_aristas)
        peso = datos_y_peso[0]
        datos = datos_y_peso[1]
        origen = datos[0]
        destino = datos[1]
        array_origen = None
        array_destino = None

        for array_conexo in bosque:
            if origen in array_conexo:
                indice = bosque.index(array_conexo)
                array_origen = bosque.pop(indice)
                break

        for array_conexo in bosque:
            if destino in array_conexo:
                indice = bosque.index(array_conexo)
                array_destino = bosque.pop(indice)
                break

        if (array_origen is not None) and (array_destino is not None):
                if (len(array_origen) > len(array_destino)) or (len(array_origen) == len(array_destino)):
                    bosque.append(array_origen + array_destino)
                else:
                    bosque.append(array_destino + array_origen)
        else:
            bosque.append(array_origen)

    return bosque[0]


def prim(grafo):
    bosque = []
    vertice_inicial = grafo.inicio
    heap_aristas = Heap(grafo.tamanio ** 2)
    aux_adyacentes = vertice_inicial.adyacentes.inicio

    if grafo:
        bosque += vertice_inicial.info

    while aux_adyacentes is not None:
        datos = [vertice_inicial.info, aux_adyacentes.destino]
        peso = aux_adyacentes.info
        arribo_H(heap_aristas, peso, datos)
        aux_adyacentes = aux_adyacentes.sig

    while (len(bosque) // 2 < grafo.tamanio) and not heap_vacio(heap_aristas):
        datos_y_prioridad = atencion_H(heap_aristas)
        datos = datos_y_prioridad[1]
        origen = datos[0]
        destino = datos[1]

        if(len(bosque) == 0 or ((origen not in bosque) or (destino not in bosque))):
            bosque += destino

            nodo_destino = buscar_vertice(grafo, destino)
            aux_adyacentes = nodo_destino.adyacentes.inicio

            while aux_adyacentes is not None:
                peso = aux_adyacentes.info
                datos = [nodo_destino.info, aux_adyacentes.destino]
                arribo_H(heap_aristas, peso, datos)
                aux_adyacentes = aux_adyacentes.sig


    return bosque


def resolverCaminoDijkstra(pila_camino, fin):
    camino = []
    while not pila_vacia(pila_camino):
        dato = desapilar(pila_camino)
        if dato[1][0].info == fin:
            camino.append(dato[1][0].info)
            fin = dato[1][1]
    return camino[::-1]  # Array invertido


def resolverCaminoDijkstraPeso(pila_camino, fin):
    pila_camino_aux = copiarPila(pila_camino)
    peso_del_camino = 0
    while not pila_vacia(pila_camino_aux):
        dato = desapilar(pila_camino_aux)
        if dato[1][0].info == fin:
            peso_del_camino += dato[0]
            fin = dato[1][1]
    return peso_del_camino


def dijkstra(grafo, origen, destino):
    no_visitados = Heap(grafo.tamanio)
    camino = Pila()
    aux_vertices = grafo.inicio

    while aux_vertices is not None:
        if aux_vertices.info == origen:
            arribo_H(no_visitados, 0, [aux_vertices, None])
        else:
            arribo_H(no_visitados, isinf, [aux_vertices, None])
        aux_vertices = aux_vertices.sig

    while not heap_vacio(no_visitados):
        dato = atencion_H(no_visitados)
        apilar(camino, dato)
        aux_adyacentes = dato[1][0].adyacentes.inicio

        while aux_adyacentes is not None:

            pos = buscar_H(no_visitados, aux_adyacentes.destino)

            distancia_acumulada = dato[0] + aux_adyacentes.info

            if (distancia_acumulada < no_visitados.vector[pos][0]):
                no_visitados.vector[pos][1][1] = dato[1][0].info
                cambiarPrioridad(no_visitados, pos, distancia_acumulada)
            aux_adyacentes = aux_adyacentes.sig

    return resolverCaminoDijkstra(camino, destino)


def dijkstra2(grafo, origen, destino):
    no_visitados = Heap(grafo.tamanio)
    camino = Pila()
    aux_vertices = grafo.inicio

    while aux_vertices is not None:
        if aux_vertices.info == origen:
            arribo_H(no_visitados, 0, [aux_vertices, None])
        else:
            arribo_H(no_visitados, isinf, [aux_vertices, None])
        aux_vertices = aux_vertices.sig

    while not heap_vacio(no_visitados):
        dato = atencion_H(no_visitados)
        apilar(camino, dato)

        aux_adyacentes = dato[1][0].adyacentes.inicio

        while aux_adyacentes is not None:
            pos = buscar_H(no_visitados, aux_adyacentes.destino)
            distancia_acumulada = dato[0] + aux_adyacentes.info

            if (distancia_acumulada < no_visitados.vector[pos][0]):
                no_visitados.vector[pos][1][1] = dato[1][0].info
                cambiarPrioridad(no_visitados, pos, distancia_acumulada)
            aux_adyacentes = aux_adyacentes.sig

    largo_de_camino = resolverCaminoDijkstraPeso(camino, destino)
    camino_resuelto = resolverCaminoDijkstra(camino, destino)

    return camino_resuelto, largo_de_camino





# ------------------ PARA EJERCICIO 1 -------------------
def listaAleatoriaVerticesSinRepetir(cantidad=10):
    lv = []
    while len(lv) < cantidad:
        info = chr(random.randint(65, 90))
        if info not in lv:
            lv.append(info)
    return lv

def verticeSinApuntar(vertice):
    return vertice.adyacentes.tamanio == 0

def verticeEsApuntado(grafo, vertice):
    apuntado = False
    aux_vertice = grafo.inicio
    while (aux_vertice is not None) and (not apuntado):
        aux_adyacentes = aux_vertice.adyacentes.inicio
        while (aux_adyacentes is not None) and (not apuntado):
            if aux_adyacentes.destino == vertice.info:
                apuntado = True
            aux_adyacentes = aux_adyacentes.sig
        aux_vertice = aux_vertice.sig

    return apuntado

def verticeDesconectado(grafo, vertice):
    return verticeSinApuntar(vertice) and (not verticeEsApuntado(grafo, vertice))

def eliminarVerticesDesconectados(grafo):
    eliminados = []
    aux_vertice = grafo.inicio
    while aux_vertice is not None:
        if verticeDesconectado(grafo, aux_vertice):
            eliminar_vertice(grafo, aux_vertice.info)
            eliminados.append(aux_vertice)
        aux_vertice = aux_vertice.sig

    return eliminados


def cantidad_aristas_apuntando(grafo):
    lista_nodos = []
    mayor_cantidad = 0
    aux_vertices = grafo.inicio
    while aux_vertices is not None:
        if aux_vertices.adyacentes.tamanio > mayor_cantidad:
            mayor_cantidad = aux_vertices.adyacentes.tamanio
            lista_nodos = [aux_vertices]
        elif aux_vertices.adyacentes.tamanio == mayor_cantidad:
            lista_nodos.append(aux_vertices)
        aux_vertices = aux_vertices.sig

    return lista_nodos


def aristas_que_apuntan(grafo, vertice):
    lista = []
    aux_vertice = grafo.inicio
    while (aux_vertice is not None):
        # Recorrida los vertices grafo
        aux_adyacentes = aux_vertice.adyacentes.inicio
        while (aux_adyacentes is not None):
            # Recorrida de las aristas de la lista de adyacencia de cada vertice
            if (aux_vertice not in lista) and (aux_adyacentes.destino == vertice.info):
                lista.append(aux_vertice)
            aux_adyacentes = aux_adyacentes.sig
        aux_vertice = aux_vertice.sig
    return lista


def cant_aristas_entrada(grafo):
    lista_nodos = []
    mayor_cantidad = 0
    aux_vertices = grafo.inicio
    while aux_vertices is not None:
        cantidad_entrantes = len(aristas_que_apuntan(grafo, aux_vertices))
        if cantidad_entrantes > mayor_cantidad:
            mayor_cantidad = cantidad_entrantes
            lista_nodos = [aux_vertices]
        elif cantidad_entrantes == mayor_cantidad:
            lista_nodos.append(aux_vertices)
        aux_vertices = aux_vertices.sig
    return lista_nodos


def vertices_sin_salidas(grafo):
    aux_vertices = grafo.inicio
    print('Vertices sin aristas de salida:')
    while aux_vertices is not None:
        if verticeSinApuntar(aux_vertices):
            print(aux_vertices.info)
        aux_vertices = aux_vertices.sig


def vertice_con_ciclo(vertice):
    aux_adyacentes = vertice.adyacentes.inicio
    while aux_adyacentes is not None:
        if aux_adyacentes.destino == vertice.info:
            return True
        aux_adyacentes = aux_adyacentes.sig

    return False

def cant_vertices_ciclo(grafo):
    cantidad_autoapuntados = 0
    aux_vertices = grafo.inicio
    while aux_vertices is not None:
        if vertice_con_ciclo(aux_vertices):
            cantidad_autoapuntados += 1
        aux_vertices = aux_vertices.sig
    return cantidad_autoapuntados


def arista_mas_larga(grafo):
    lista = []
    distancia_maxima = 0
    aux_vertice = grafo.inicio
    while (aux_vertice is not None):
        aux_adyacentes = aux_vertice.adyacentes.inicio
        while (aux_adyacentes is not None):
            distancia = aux_adyacentes.info
            if distancia > distancia_maxima:
                distancia_maxima = distancia
                ori = aux_vertice.info
                des = aux_adyacentes.destino
                lista = [[ori, des, distancia]]
            elif distancia == distancia_maxima:
                ori = aux_vertice.info
                des = aux_adyacentes.destino

                lista.append([ori, des, distancia])
            aux_adyacentes = aux_adyacentes.sig
        aux_vertice = aux_vertice.sig
    return lista


# ------------------ PARA EJERCICIO 2 -------------------
def camino_dir(grafo, origen, destino):
    origen = buscar_vertice(grafo, origen)
    if origen is not None:
        aux_aristas = origen.adyacentes.inicio
        while aux_aristas is not None:
            if aux_aristas.destino == destino:
                return True
            aux_arsitas = aux_aristas.sig
    return False


def lista_vertices(grafo):
    lista = []
    aux = grafo.inicio
    while aux is not None:
        lista.append(aux.info)
        aux = aux.sig
    return lista


def lista_por_linea(grafo, lista1, origen):
    lista = []
    for destino in lista1:
        if camino_dir(grafo, origen.info, destino):
            lista.append('1')
        else:
            lista.append('0')
    return lista


def mostrar_arreglo_ady(grafo):
    l = lista_vertices(grafo)
    print('  ' + '  '.join(l))
    print('------------------')
    aux = grafo.inicio
    while aux is not None:
        lis_linea = lista_por_linea(grafo, l, aux)
        print(aux.info + ' | ' + '  '.join(lis_linea))
        aux = aux.sig


def lista_lista_ady(vertice):
    lista = []
    aux = vertice.adyacentes.inicio
    while aux is not None:
        lista.append(aux.destino)
        aux = aux.sig
    return lista


def mostrar_lista_lista_ady(grafo):
    aux = grafo.inicio
    while aux is not None:
        lista_ady = lista_lista_ady(aux)
        print('Vertices:', aux_vertices.info, 'Aristas:', ' >> '.join(lista_ady))
        print()
        aux = aux.sig




# ------------------ PARA EJERCICIO 3 -------------------
class Antena():

    def __init__(self, id, lat, lon, vel_transf):
        self.info = id
        self.ubicacion = [lat, lon]
        self.vel_transf = vel_transf
        self.sig = None
        self.visitado = False
        self.adyacentes = lista_arista()

    def __str__(self):
        return "Id: " + str(self.info) + "\nUbicacion: " + str(self.ubicacion) + "\nVel. de transf.: " + str(self.vel_transf) + "MB/s"


def antena_trasmite(id=-1):
    if id == -1:
        identificador = random.randint(0, 200)
    else:
        identificador = id
    lat = random.randint(-100, 100)
    long = random.randint(-100, 100)
    trans = random.randint(100, 500)

    return Antena(identificador, lat, long, trans)


def insertar_objeto(grafo, objeto):
    vertice = objeto
    if (grafo.inicio is None) or (vertice.info < grafo.inicio.info):
        vertice.sig = grafo.inicio
        grafo.inicio = vertice
    else:
        act = grafo.inicio.sig
        ant = grafo.inicio
        while (act is not None) and (act.info <= vertice.info):
            act = act.sig
            ant = ant.sig
        vertice.sig = act
        ant.sig = vertice
    grafo.tamanio += 1


# ------------------ PARA EJERCICIO 4 -------------------
class Red():

    def __init__(self, tipo, nombre):
        self.info = nombre
        self.tipo = tipo
        self.sig = None
        self.visitado = False
        self.adyacentes = lista_arista()



# ------------------ PARA EJERCICIO 7 -------------------

class Persona():

    def __init__(self, nombre, apellido):
        self.info = nombre
        self.apellido = apellido
        self.sig = None
        self.visitado = False
        self.adyacentes = lista_arista()

def cargar_persona(grafo):
    datos = [
        Persona('A', 'Med'),
        Persona('B', 'Bou'),
        Persona('C', 'Bon'),
        Persona('D', 'Eul'),
        Persona('E', 'Bel'),
        Persona('F', 'Vel'),
        Persona('G', 'Gut'),
        Persona('Y', 'Cas'),
        Persona('X', 'Alr')
    ]
    for elemento in datos:
        insertar_objeto(grafo, elemento)


def cargar_arista_persona(grafo):
    redes = ['TW', 'FB', 'IG']
    for i in range(15):
        red = random.choice(redes)
        rt = random.randint(0,100)
        lista = lista_vertices(grafo)
        origen = random.choice(lista)
        destino = random.choice(lista)

        insertar_arista(grafo, [red, rt], origen, destino)


def peso_max_aristas(grafo, redsocial):
    peso_max = -1
    aux_vertices = grafo.inicio

    while aux_vertices is not None:
        aux_adyacentes = aux_vertices.adyacentes.inicio

        while aux_adyacentes is not None:
            red = aux_adyacentes.info[0]
            peso = aux_adyacentes.info[1]

            if (red == redsocial) and (peso > peso_max):
                peso_max = peso
            aux_adyacentes = aux_adyacentes.sig
        aux_vertices = aux_vertices.sig

    return peso_max


def kruskal_rs(grafo, red_social):
    bosque = []
    heap_aristas = Heap(grafo.tamanio**2)

    peso_maximo = peso_max_aristas(grafo, red_social)
    aux_vertices = grafo.inicio

    while aux_vertices is not None:
        bosque.append([aux_vertices.info])
        adyacentes = aux_vertices.adyacentes.inicio

        while adyacentes is not None:
            if adyacentes.info[0] == red_social:
                datos = [aux_vertices.info, adyacentes.destino]
                peso = peso_maximo - adyacentes.info[1]
                arribo_H(heap_aristas, peso, datos)
            adyacentes = adyacentes.sig
        aux_vertices = aux_vertices.sig

    while (len(bosque) > 1) and (not heap_vacio(heap_aristas)):
        datos_y_peso = atencion_H(heap_aristas)
        peso = datos_y_peso[0]
        datos = datos_y_peso[1]

        origen = datos[0]
        destino = datos[1]
        array_origen = None
        array_destino = None

        for array_conexo in bosque:
            if origen in array_conexo:
                indice = bosque.index(array_conexo)
                array_origen = bosque.pop(indice)
                break
        for array_conexo in bosque:
            if destino in array_conexo:
                indice = bosque.index(array_conexo)
                array_destino = bosque.pop(indice)
                break

        if (array_origen is not None) and (array_destino is not None):
                if (len(array_origen) > len(array_destino)) or (len(array_origen) == len(array_destino)):
                    bosque.append(array_origen + array_destino)
                else:
                    bosque.append(array_destino + array_origen)
        else:
            bosque.append(array_origen)

    return bosque[0]


def existe_camino_RS(grafo, vertice, destino, red_social):

    cola = Cola()

    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            arribo(cola, vertice)

            while not cola_vacia(cola):
                nodo = atencion(cola)
                if nodo.info == destino:
                    return True

                aux_adyacentes = nodo.adyacentes.inicio
                while aux_adyacentes is not None:
                    if aux_adyacentes.info[0] == red_social:
                        resultado = buscar_vertice(grafo, aux_adyacentes.destino)

                        if not resultado.visitado:
                            resultado.visitado = True
                            arribo(cola, resultado)

                    aux_adyacentes = aux_adyacentes.sig
        vertice = vertice.sig

    return False

# ------------------ PARA EJERCICIO 10 -------------------
class Lugar():

    def __init__(self, nombre, latitud, longitud):
        self.info = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.sig = None
        self.visitado = False
        self.adyacentes = lista_arista()

    def __str__(self):
        return "Nombre: " + self.info + " - Lat: " + str(self.latitud) + " - Long: " + str(self.longitud)

def cargar_puntos(grafo, puntos):
    for punto in puntos:
        lat = random.randint(-100, 100)
        long = random.randint(-100, 100)
        lugar = Lugar(punto, lat, long)
        insertar_objeto(grafo, lugar)

def cargar_aristas_puntos(grafo, puntos):
    for punto in puntos:
        vertice = buscar_vertice(grafo, punto)
        for lugar in puntos:
            if (punto != lugar) and (buscar_arista(vertice, lugar) is None):
                dist = random.randint(0,100)
                insertar_arista(grafo, dist, vertice.info, lugar)
