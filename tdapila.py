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
        dato = random.randint(0, 20)
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
    return pila.tope == -1


def tamanio(pila):
    return pila.tope + 1


def cima(pila):
    return pila.datos[pila.tope]


def barrido(pila):
    paux = Pila()
    while not pila_vacia(pila):
        dato = desapilar(pila)
        print(dato)
        apilar(paux, dato)
    while not pila_vacia(paux):
        apilar(pila, desapilar(paux))


def invertir(pila, paux):
    while not pila_vacia(pila):
        dato = desapilar(pila)
        print(dato)
        apilar(paux, dato)


def randString(largo):
    letras = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(largo):
        return ''.join((random.choice(letras) for i in range(largo)))


def listaRandom(tamanio):
    lista = []
    for i in range(0, tamanio):
        lista.append(random.randint(-100, 100))

    return lista


def dirrecionAnum(dir):
    n = 0
    if (dir == "norte"):
        n = 1
    elif (dir == "sur"):
        n = 5
    elif (dir == "oeste"):
        n = 7
    elif (dir == "este"):
        n = 3
    elif (dir == "noreste"):
        n = 2
    elif (dir == "noroeste"):
        n = 8
    elif (dir == "sureste"):
        n = 4
    elif (dir == "suroeste"):
        n = 6
    return n


def numAdirrecion(n):
    dir = ""
    if (n == 1):
        dir = "norte"
    elif (n == 2):
        dir = "noreste"
    elif (n == 3):
        dir = "este"
    elif (n == 4):
        dir = "sureste"
    elif (n == 5):
        dir = "sur"
    elif (n == 6):
        dir = "suroeste"
    elif (n == 7):
        dir = "oeste"
    elif (n == 8):
        dir = "noreste"
    return dir


# NO ORDENA
def quicksortI(vec, pri, ult):
    pila = Pila()
    apilar(pila, [pri, ult])
    #dato = []
    while not pila_vacia(pila):
        dato = desapilar(pila)
        i = dato[0]
        j = dato[1] - 1
        pivote = dato[1]
        while (i < j):
            while (vec[i] <= vec[pivote]):
                i += 1
            while (vec[j] > vec[pivote]):
                j -= 1
            if i < j:
                vec[i], vec[j] = vec[j], vec[i]
        if vec[pivote] < vec[i]:
            vec[pivote], vec[i] = vec[i], vec[pivote]

        if dato[0] < i:
            apilar(pila, [dato[0], j])
        if dato[1] > i:
            apilar(pila, [i+1, dato[1]])


def ordencre(pila):
    aux = Pila()
    while not pila_vacia(pila):
        cont = 0
        dato = desapilar(pila)
        while not pila_vacia(aux) and (cima(aux)[1] >= dato[1]):
            apilar(pila, desapilar(aux))
            cont += 1
        apilar(aux, dato)
        for i in range(0, cont):
            apilar(aux, desapilar(pila))
    return aux


def ordendec(pila):
    aux = Pila()
    while not pila_vacia(pila):
        cont = 0
        dato = desapilar(pila)
        while not pila_vacia(aux) and (cima(aux)[1] <= dato[1]):
            apilar(pila, desapilar(aux))
            cont += 1
        apilar(aux, dato)
        for i in range(0, cont):
            apilar(aux, desapilar(pila))
    return aux
