def crear(grado):
    pol = []
    for i in range(0, grado + 1):
        pol.append(0)
    return pol


def cargar(pol, termino, valor):
    if termino <= grado(pol):
        pol[termino] = valor


def grado(pol):
    return (len(pol) - 1)


def suma(pol1, pol2):
    pol3 = crear(grado_mayor(pol1, pol2))
    for i in range(0, grado(pol3) + 1):
        if i <= grado(pol1) and i <= grado(pol2):
            cargar(pol3, i, pol1[i] + pol2[i])
        else:
            if grado(pol1) > grado(pol2):
                cargar(pol3, i, pol1[i])
            else:
                cargar(pol3, i, pol2[i])
    return pol3


def grado_mayor(pol1, pol2):
    if (grado(pol1) > grado(pol2)):
        return grado(pol1)
    else:
        return grado(pol2)


def producto(pol1, pol2):
    pol3 = crear(grado(pol1) + grado(pol2))
    for i in range(0, grado(pol1) + 1):
        for j in range(0, grado(pol2) + 1):
            cargar(pol3, i + j, (pol1[i] * pol2[j]) + pol3[i + j])
    return pol3
