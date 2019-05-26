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


def cargautomatica1(cola):
    while not cola_llena(cola):
        dato = random.randint(0, 20)
        arribo(cola, dato)


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


'''def ordencrec(cola):
    num = int(input("Ingrese el numero que desea agregar: "))
    cola1 = Cola()
    while not cola_vacia(cola) and (cola.frente < num):
        arribo(cola1, atencion(cola))
    arribo(cola1, num)
    while not cola_vacia(cola):
        arribo(cola1, atencion(cola))'''



'''def randString(largo):
    letras = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(largo):
        return ''.join((random.choice(letras) for i in range(largo)))'''
