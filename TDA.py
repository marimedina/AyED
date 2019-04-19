
def crear(grado):
    pol = []
    for i in range(0, grado):
        pol.append(0)
    return pol


def grado(pol):
    return len(pol)-1


def cargar(pol, termino, valor):
    if termino < grado(pol):
        pol[termino] = valor


def suma(pol1, pol2):
    '''crear pol3 del tamaño del mayor entre pol1 y pol2'''
    for i in range(0, grado):
        if i < grado(pol1) and i <= grado(pol2):
            cargar(pol3, i, pol[i] + pol[j]
        else:
            if grado(pol1) > grado(pol2):
                cargar(pol3, i, pol1)
            else:
                cargar(pol3, i, pol2)


def producto(pol1, pol2):
    pol3 = crear(grado(pol1) + grado(pol2))
    for i in range(0, grado(pol1)):
        for j in range(0, grado(pol2)):
            cargar(pol3, i + j, (pol1[i] * pol2[j]) + pol3[i+j])
