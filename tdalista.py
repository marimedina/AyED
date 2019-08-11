import random


class nodoLista():
    info, sig = None, None


class Lista():
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def cargaAuto(lista, cantidad):
    for i in range(0, cantidad):
        insertar(lista, random.randint(0, 50))


def cargaString(lista, cantidad):
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0, cantidad):
        insertar(lista, random.choice(abc))


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
    dato = None
    if lista.inicio.info == clave:
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamanio -= 1
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while (act is not None) and (act.info < clave):
            ant = ant.sig
            act = act.sig
        if (act is not None) and (act.info == clave):
            dato = act.info
            ant.sig = act.sig
            lista.tamanio -= 1
    return dato


def barrido(lista):
    aux = lista.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.sig


def lista_vacia(lista):
    return lista.tamanio == 0


def tamanio(lista):
    return lista.tamanio


def busqueda(lista, buscado):
    buscado = -1
    i = -1
    aux = lista.inicio
    while (aux is not None) and (buscado == -1):
        i += 1
        if (aux.info == buscado):
            pos = i
        aux = aux.sig

    return pos
