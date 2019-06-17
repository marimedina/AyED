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


# CONCATENAR


def cargaturnos(cola):
    letras = "ABCDE"
    while not cola_llena(cola):
        dato = random.choice(letras)
        dat = random.randint(000, 999)
        arribo(cola, dato)
        arribo(cola, dat)


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

'''def fibcola(n):
    cola = Cola()
    arribo(cola, 0)
    if (n == 1):
        arribo(cola, 1)
    elif (n > 1):
        arribo(cola, 1)
        while not cola_llena(cola) and cola.datos[cola.final] <= n:
            dato = atencion(cola)
            dato2 = cola.datos[cola.final]
            arribo(cola, dato)
            d = dato + dato2
            arribo(cola, d)
    barridoc(cola)'''

'''def ordencrec(cola):
    num = int(input("Ingrese el numero que desea agregar: "))
    cola1 = Cola()
    while not cola_vacia(cola) and (cola.frente < num):
        arribo(cola1, atencion(cola))
    arribo(cola1, num)
    while not cola_vacia(cola):
        arribo(cola1, atencion(cola))'''
