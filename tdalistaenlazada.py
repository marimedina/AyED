import random
import math
import string


class Lista():
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


class ListadeLista():
    info, sig, lista = None, None, Lista()


def insertar(lista, dato):
    nodo = ListadeLista()
    nodo.info = dato
    # resuelve primer caso y segundo
    if (lista.inicio is None) or (nodo.info < lista.inicio.info):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        # resuelve tercer y cuarto caso
        act = lista.inicio.sig
        ant = lista.inicio
        while (act is not None) and (act.info <= nodo.info):
            act = act.sig
            ant = ant.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamanio += 1
