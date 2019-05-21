class nodoLista():
    info, sig = None, None


class Lista():
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def insertar(lista, dato):
    nodo = nodoLista()
    nodo.info = dato
    # resuelve primer caso y segundo
    if (lista.inicio is None) or (nodo.info < lista.inicio.info):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        # resuelve tercer y cuarto caso
        act = lista.inicio.sig
        ant = lista.inicio
        while (act is not None) and (act.info < nodo.info):
            act = act.sig
            ant = ant.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamanio += 1


 

def eliminar(lista, clave):



def barrido(lista):
    aux = lista.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.sig
