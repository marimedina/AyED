import random
max = 20


class Pila():

    def __init__(self):
        self.tope = -1
        self.datos = []
        for i in range(0, max):
            self.datos.append(None)


def cargautomatica(pila):
    while not pila_llena(pila):
        dato = random.randint(0, 10)
        apilar(pila, dato)


def apilar(pila, dato):
    pila.tope += 1
    pila.datos[pila.tope] = dato


def desapilar(pila):
    dato = pila.datos[pila.tope]
    pila.tope -= 1
    return dato


def pila_llena(pila):
    return pila.tope + 1 == max


def pila_vacia(pila):
    return pila.tope - 1 == -1


def tamanio(pila):
    return pila.tope + 1


def cima(pila):
    return pila.dato[pila.tope]


def barrido(pila):
    paux = pila()
    while not pila_vacia(pila):
        dato = desapilar(pila)
        print(dato)
        apilar(paux, dato)


def invertir(pila, paux):
    while not pila_vacia(pila):
        dato = desapilar(pila)
        print(dato)
        apilar(paux, dato)


def randString(largo):
    letras = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(largo):
        return ''.join((random.choice(letras) for i in range(largo)))
