import random
import math
import string


class nodoLista():
    info, sig, ant = None, None, None


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
        while (act is not None) and (act.info <= nodo.info):
            act = act.sig
            ant = ant.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamanio += 1


def insertar1(lista, dato, posicion):
    nodo = nodoLista()
    nodo.info = dato
    aux = lista.inicio
    if (posicion >= 0) and (posicion <= lista.tamanio):
        if (posicion == 0):
            nodo.sig = lista.inicio
            lista.inicio = nodo
        elif (posicion < lista.tamanio):
            for i in range(1, posicion):
                aux = aux.sig
            nodo.sig = aux.sig
            aux.sig = nodo
        else:
            while aux.sig is not None:
                aux = aux.sig
            aux.sig = nodo
    else:
        print("El indice " + str(posicion) + " excede el tamaño de elementos que ")
        print("posee la lista")


def eliminarNodo(lista):
    aux = None
    if lista.inicio is not None:
        aux = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamanio -= 1
    return aux


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


def busquedaLista(l, buscado):
    """Devuelve dirección de memoria. None si no se encontró lo buscado"""
    aux = l.inicio
    while (aux is not None) and (aux.info != buscado):
        aux = aux.sig

    return aux


'''def busqueda(lista, buscado):
    buscado = -1
    i = -1
    aux = lista.inicio
    while (aux is not None) and (buscado == -1):
        i += 1
        if (aux.info == buscado):
            pos = i
        aux = aux.sig
    return pos'''


def primo(num):
    pri = True
    if num < 2 and num != 0:
        return True
    elif num == 2:
        return True
    else:
        i = 2
        while (i <= math.sqrt(num)) and pri:
            if (i != num) and (num % i == 0):
                pri = False
            i += 1
        return pri


def campos(lista, dato, i):
    nodo = nodoLista()
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


'''def ubicar(lista, pos):
    valor = lista[pos]
    j = pos
    while j > 0 and valor < lista[j-1]:
        lista[j] = lista[j-1]
        j -= 1
    lista[j] = valor


def ord_alf(lista):
    for i in range(len(lista)-1):
        if lista[i+1] < lista[i]:
            ubicar(lista, i+1)'''


def pokemones(cantidad):
    lista = Lista()
    pokemones = ['Bulbasaur', 'Ivysaur', 'Charmander', 'Squirtle', 'Caterpie']
    tipos = ['fuego', 'agua', 'planta', 'bicho', 'normal', 'veneno', 'electrico']
    for i in range(0, 10):
        nomb = random.choice(pokemones)
        nivel = random.randint(1, 40)
        tipo = random.choice(tipos)
        subtipo = random.choice(string.ascii_uppercase)
        pok = [nomb, nivel, tipo, subtipo]
        campos(lista, pok, 0)
    return lista
