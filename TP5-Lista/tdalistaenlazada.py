import random
import math
import string


class Lista2():
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


class ListadeLista():

    def __init__(self):
        self.info = None
        self.sig = None
        self.lista = Lista2()


def tamanio2(lista):
    return lista.tamanio


def insertar2(lista, dato):
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


def barrido2(lista):
    aux = lista.inicio
    while aux is not None:
        print(aux.info)
        dato = aux.lista.inicio
        while dato is not None:
            print(dato.info)
            dato = dato.sig
        aux = aux.sig


def busquedaLista2(lista, buscado):
    """Devuelve direccion de memoria. None si no se encontro lo buscado"""
    aux = lista.inicio
    while (aux is not None) and (aux.info != buscado):
        aux = aux.sig
    return aux


def busquedacampos2(lista, buscado, campo):
    aux = lista.inicio
    while aux is not None and aux.info[campo] != buscado:
        aux = aux.sig
    return aux


def campos2(lista, dato, i):
    nodo = ListadeLista()
    nodo.info = dato
    if (lista.inicio is None) or (nodo.info[i] < lista.inicio.info[i]):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while (act is not None) and (act.info[i] <= nodo.info[i]):
            act = act.sig
            ant = ant.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamanio += 1
