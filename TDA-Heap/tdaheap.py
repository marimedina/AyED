class heap():
    def __init__(self, tamanio):
        self.tamanio = 0
        self.vector = [None]*tamanio


def intercambio(a, b):
    a, b = b, a


def flotar(H, indice):
    padre = (indice-1)//2
    while ((padre >= 0) and (H.vector[padre] < H.vector[indice])):
        intercambio((H.vector[padre]), (H.vector[indice]))
        padre = ((padre-1)//2)


def agregar(H, dato):
    H.vector[H.tamanio] = dato
    flotar(H, H.tamanio)
    H.tamanio += 1


def hundir(H, indice):
    HI = (indice*2)+1
    control = True
    while (control and HI < H.tamanio-1):
        MAY = HI
        HD = HI+1
        if (HI <= H.tamanio-1) and (H.vector[HD] > H.vector[HI]):
            MAY = HD
        if (H.vector[indice] < H.vector[MAY]):
            intercambio((H.vector[indice]), (H.vetor[MAY]))
        else:
            control = False
            HI = (2*MAY)+1


def quitar(H):
    intercambio((H.vector[0]), (H.vector[H.tamanio-1]))
    H.tamanio -= 1
    hundir(H, 0)
    return(H.vector[H.tamanio+1])


# cola de proridad
def arribo_H(H, prioridad, dato):
    agregar(H, [prioridad, dato])


def atencio_H(H):
    aux = quitar(H)
    return(aux)


def Heapsort(H):
    aux = H.tamanio
    for i in H.tamanio-2:
        quitar(H)
        H.tamanio = aux

def monticulizar(H):
    for i in len(H.vector):
        flotar(H)
