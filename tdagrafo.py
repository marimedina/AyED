import tdacola


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

'''en el insertar arista hago una busqueda de origen y destino, si ambos
son verdaderas entonces le paso el destino'''
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
