class Heap():
    def __init__(self, tamanio):
        self.tamanio = 0
        self.vector = [None] * tamanio


def intercambio(vector, indice1, indice2):
    vector[indice1], vector[indice2] = vector[indice2], vector[indice1]


def agregar(heap, dato):
    heap.vector[heap.tamanio] = dato
    flotar(heap, heap.tamanio)
    heap.tamanio += 1


def quitar(heap):
    primer_elemento = heap.vector[0]
    intercambio(heap.vector, 0, heap.tamanio-1)
    heap.tamanio -= 1
    hundir(heap, 0)
    return primer_elemento


def flotar(heap, indice):
    padre = (indice - 1) // 2
    while (indice > 0) and (heap.vector[indice][0] < heap.vector[padre][0]):
        intercambio(heap.vector, indice, padre)
        indice = padre
        padre = (indice - 1) // 2


def hundir(heap, indice):
    indice_hijo_izq = (2 * indice) + 1
    control = True

    while control and (indice_hijo_izq < heap.tamanio):
        indice_hijo_der = indice_hijo_izq + 1
        # Ve cual de los hijos es mayor
        indice_menor = indice_hijo_izq

        if (indice_hijo_der < heap.tamanio):
            if (heap.vector[indice_hijo_der][0] < heap.vector[indice_hijo_izq][0]):
                indice_menor = indice_hijo_der

        if heap.vector[indice][0] > heap.vector[indice_menor][0]:
            # Intercambio con el hijo que haya tenido menor num de prioridad
            intercambio(heap.vector, indice, indice_menor)
            indice = indice_menor
            indice_hijo_izq = (indice * 2) + 1
        else:
            control = False


def atencion_H(heap):
    return quitar(heap)


def arribo_H(heap, prioridad, dato):
    agregar(heap, [prioridad, dato])


def heapSort(heap):
    aux = heap.tamanio
    for i in range(0, heap.tamanio):
        quitar(heap)
    heap.tamanio = aux


def buscar_H(heap, buscado):
    for i in range(len(heap.vector)):
        if heap.vector[i][1][0].info == buscado:
            return i
    return -1


def barridoMonticulo(heap):
    for i in range(heap.tamanio):
        print(heap.vector[i])


def monticulizar(heap):
    for indice in range(len(heap.vector)):
        flotar(heap, indice)


def heap_vacio(heap):
    return heap.tamanio == 0


def heap_lleno(heap):
    return heap.tamanio == len(heap.vector)


def cambiarPrioridad(heap, indice, prioridad):
    prioridad_anterior = heap.vector[indice][0]
    heap.vector[indice][0] = prioridad
    if(prioridad < prioridad_anterior):
        flotar(heap, indice)
    elif(prioridad > prioridad_anterior):
        hundir(heap, indice)
