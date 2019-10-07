class nodoArista():
    info, sig, peso = None, None, 0


class nodoVertice():
    info, sig, ady = None, None, nodoArista()


class Arista():
    inicio, tamanio = None, 0


class Grafo():
    inicio, tamanio = None, 0


def insertar_vertice(grafo, dato):
    nodo = nodoVertice
    nodo.info = dato
    if grafo.inicio is None or nodo.info < grafo.inicio.info:
        nodo.sig = grafo.inicio




'''en el insertar arista hago una busqueda de origen y destino, si ambos
son verdaderas entonces le paso el destino'''
