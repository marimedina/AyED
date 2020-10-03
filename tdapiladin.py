import random


class NodoPila():
    info, sig = None, None


class Pila():
    def __init__(self):
        self.tamanio = 0
        self.tope = None


def apilar(pila, dato):
    aux = NodoPila()
    aux.info = dato
    aux.sig = pila.tope
    pila.tope = aux
    pila.tamanio += 1


def desapilar(pila):
    dato = pila.tope.info
    pila.tope = pila.tope.sig
    pila.tamanio -= 1
    return dato


def pila_llena(pila):
    return False


def pila_vacia(pila):
    return pila.tope is None


def tamanio(pila):
    return pila.tamanio


num = 10


def cargautomatica(pila):
    while tamanio(pila) <= num:
        dato = random.randint(0, 10)
        apilar(pila, dato)
