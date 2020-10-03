max = 20
import random


class Cola():
    def __init__(self):
        self.datos = []
        for i in range(0, max):
            self.datos.append(None)
        self.frente = 0
        self.final = -1
        self.tamanio = 0


def arribo(cola, dato):
    cola.final += 1
    if cola.final == max:
        cola.final = 0
    cola.datos[cola.final] = dato
    cola.tamanio += 1


def atencion(cola):
    aux = cola.datos[cola.frente]
    cola.frente += 1
    cola.tamanio -= 1
    if cola.frente == max:
        cola.frente = 0
    return aux


def cola_vacia(cola):
    return cola.tamanio == 0


def cola_llena(cola):
    return cola.tamanio == max


def tamanioc(cola):
    return cola.tamanio


def barridoc(cola):
    caux = Cola()
    while not cola_vacia(cola):
        aux = atencion(cola)
        print(aux)
        arribo(caux, aux)
    while not cola_vacia(caux):
        aux = atencion(caux)
        arribo(cola, aux)


def mover_al_final(cola):
    aux = atencion(cola)
    arribo(cola, aux)


def cargaAutoStr(cola):
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while (not cola_llena(cola)):
        arribo(cola, random.choice(abc))


def cargautomatica1(cola):
    while not cola_llena(cola):
        dato = random.randint(0, 20)
        arribo(cola, dato)


def cargacaract(cola):
    caract = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.;/*-+=%#!?"
    while not cola_llena(cola):
        arribo(cola, random.randint(0, 20))
        arribo(cola, random.choice(caract))


def primo(n):
    pri = True
    if n < 2:
        return True
    elif n == 2:
        return True
    else:
        i = 2
        while (i < n) and pri:
            if (n % i == 0):
                pri = False
            i += 1
        return pri
