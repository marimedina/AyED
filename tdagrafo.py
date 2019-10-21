import tdacola
from tdapila import apilar, Pila
from tdaheap atencio_H
from math import inf


class nodoArista():
    info, sig, peso = None, None, 0

    def __init__(self, info, destino):
        self.inicio = info
        self.destino = destino
        self.sig = None


class Arista():
    inicio, tamanio = None, 0


class lista_arista():
    '''lista de lista, crea lista vacia'''
    def __init__(self, dirigido=True):
        self.inicio = None
        self.tamanio = 0


class nodoVertice():
    info, sig, ady = None, None, Arista()

    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacente = lista_arista()


class Grafo():
    inicio, tamanio = None, 0


def insertar_vertice(grafo, dato):
    nodo = nodoVertice
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


def agregar_arista():


def insertar_arista(grafo, dato, origen, destino):
    if grafo.dirigido:
        agregar_arista(origen.adyacente, dato, destino.info)
    else:
        agregar_arista(origen.adyacente, dato, destino.info)
        agregar_arista(destino.info, dato, origen.adyacente)


def buscar_arista(vertice, buscado):
    aux = vertice.adyacente.inicio
    while (aux is not None) and (aux.destino != buscado):
        aux = aux.sig
    return aux


def buscar_vertice(grafo, buscado):
    aux = grafo.inicio
    while (aux is not None) and (aux.info != buscado):
        aux = aux.sig
    return aux


def adyacente(vertice):
    '''completar'''


def barrido_profundiad(grafo, vertice):
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            print(vertice.info)
            adyacente = vertice.adyacente.inicio
            while adyacente is not None:
                adyacente = buscar_vertice(grafo, adyacente.destino)
                if not adyacente.visitado:
                    barrido_profundiad(grafo, adyacente)
                adyacente = adyacente.sig
    vertice = vertice.sig


def barrido_amplitud(grafo, vertice):
    cola = Cola()
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            arribo(cola, vertice)
            while not cola vacia(cola):
                nodo = atencion(cola)
                print(nodo.info)
                adyacentes = nodo.adyacente.inicio
                while dyacente is not None:
                    adyacente = buscar_vertice(grafo, adyacente.destino)
                    if not adyacente.visitado:
                        adyacente.visitado = True
                        arribo(cola, adyacente)
                    adyacente = adyacente.sig
    vertice = vertice.sig

# terminar
def existe_paso():
    resultado = true
    if not origen.visitado:
        origen.visitado = true
        vadyacente = origen.adyacente.inicio
        while vadyacente is not none and not resultado:
            adyacente = buscar_vertice(grafo, vadyacente.origen)


def marcar_no_visitado(grafo):
    aux = grafo.inicio
    while aux is not none:
        aux.visitado = False
    aux = aux.sig


def camino_corto()


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
            eliminar_arista(aux.adyacentes, dato)
    return dato


def eliminar_arista(vertice, clave):
    dato = None
    if vertice.inicio.info == clave:
        dato = vertice.inicio.info
        vertice.inicio = vertice.inicio.sig
        vertice.tamanio -= 1
    else:
        ant = vertice.inicio
        act = vertice.inicio.sig
        while (act is not None) and (act.info != clave):
            ant = act
            act = act.sig
        if (act is not None):
            dato = act.info
            ant.sig = act.sig
            vertice.tamanio -= 1
    return dato


'''en el insertar arista hago una busqueda de origen y destino, si ambos
son verdaderas entonces le paso el destino
Adyacentes es la lista de adyacente, y adyacente es cada uno'''
'''pos = buscar_vertice()
pos_aux = buscar_arista()
if pos is not None:
    print('esta')
else:
    print('no esta')'''

# para insertar
'''origen = buscar_vertice(grafo, 'A')
destino = buscar_arista(origen, )
if origen is not None and destino si not None:
    insertar_arista(grafo, 20, origen, destino)'''


def Kruskal(grafo):
    bosque = []
    aristas = Heap(tamanio(grafo)**2)
    aux = grafo.inicio
    while aux is not None:
        bosque.append([aux.info])
        adyacentes = aux.adyacentes.inicio
        while adyacentes is not None:
            arribo_H(arista, [aux.info, adyacentes.destino], adyacentes.info)
            adyacentes = adyacentes.sig
        aux = aux.sig
    while len(bosque[0]) == 1 and not heap_vacio(aristas):
        dato = atencion_H(aristas)
        origen = None
        for elemento in bosque:
            if dato[1][0] in elemento:
                origen = bosque.pop(bosque.index(elemento))
        destino = None


def dijkstra(grafo, origen, destino):
    no_visitados = Heap(tamanio(grafo))
    camino = Pila()
    aux = grafo.inicio
    while aux is not None:
        if aux.info = origen:
            arribo_H(no_visitado, [aux, None], 0)
        else:
            arribo_H(no_visitados, [aux, None], inf)
        aux = aux.sig
    while not heap_vacio(no_visitados):
        dato = atencio_H(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while aux is not None:
            pos = buscar_H(no_visitados, aux.destino)
            if (no_visitados.vector[pos][0] > dato[0] + aux.info):
                no_visitados.vector[pos][1][1] = dato[1][0].info

                
'''cambiar prioridad es de heap'''


'''Para probar'''
'''camino = dij()
fin =
while not pila_vacia(camino):
    dato = desapilar(camino)
    if fin == dato[1][0].info:
        print('de', dato[1][0].info, 'hasta', dato[1][1], dato[0])
        fin = dato[1][1]'''
