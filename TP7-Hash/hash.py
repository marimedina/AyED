from tdalista import *
import random


def crear_tabla_abierta(tamanio):
    tabla = []
    for i in range(0, tamanio):
        tabla.append(Lista())
    return tabla


def barrido_abierta(tabla):
    for lista in tabla:
        if lista.tamanio != 0:
            barrido(lista)


def crear_tabla_cerrada(tamanio):
    tabla = []
    for i in range(0, tamanio):
        tabla.append(None)
    return tabla


def barrido_cerrada(tabla):
    for elemento in tabla:
        if elemento is not None:
            print(elemento)


def eliminar_palabra(tabla, palabra):
    indice = hash(palabra)
    if busquedaListaCampo(tabla[indice], palabra, 0) is not None:
        eliminar_por_campo(tabla[indice], palabra, 0)


def rehash(tabla, original):
    indice = original + 1
    if indice == len(tabla):
        indice = 0
    while (tabla[indice] is not None) and (indice != original):
        indice += 1
        if indice == len(tabla):
            indice = 0

    if indice == original:
        indice = None

    return indice


def hash(palabra):
    if len(palabra) > 0:
        clave = ord(palabra[0].capitalize()) - 65
    return clave


def hash_1(clave):
    indice = 0
    for elemento in clave:
        indice += ord(elemento)
    return indice


def insertar_tablaCerrada(tabla, hash, dato):
    '''Agrega elementos a una tabla cerrada'''
    pos = hash(dato, tabla)
    if tabla[pos] is None:
        tabla[pos] = dato
    else:
        if pos == len(tabla)-1:
            pos = -1
        pos_aux = pos
        while tabla[pos+1] is not None and hash(tabla[pos+1], tabla) == pos_aux:
            pos += 1
            if pos == len(tabla)-1:
                pos = -1
        if tabla[pos+1] is None:
            tabla[pos+1] = dato
        else:
            pass
            # print('hacer rehashing')


def insert_palabra(tabla, palabra, descripcion):
    clave = hash(palabra)
    indice = clave % len(tabla)
    campos(tabla[indice], [palabra, descripcion], 0)


def busq_palabra(tabla, palabra):
    indice = hash(palabra)
    return busquedaListaCampo(tabla[indice], palabra, 0)


'PARA EJERCICIO 1'
def telefono():
    caract = ''
    num = ''
    for i in range(0, random.randint(3, 5)):
        caract += str(random.randint(0, 6))
    for i in range(0, random.randint(7, 9)):
        num += str(random.randint(0, 9))
    telefono = caract + '-' + num
    return telefono


def docente(tabla, catedra):
    nombre = "Docente " + str(random.randint(0, 20))
    indice = busq_catedra(tabla, catedra)
    if indice is not None:
        insertar(tabla[indice][4], nombre)


def nueva_catedra():
    docente = Lista()
    codigo = random.randint(0, 100)
    nombre_catedra = "Nombre" + str(random.randint(0, 9))
    modalidad = random.choice(["Anual", "Cuatrimestral"])
    cantidad_horas = random.randint(1, 20)
    catedra = [codigo, nombre_catedra, modalidad, cantidad_horas, docente]
    return catedra


def busq_catedra(tabla, catedra):
    clave = hash(catedra[0])
    indice = clave % len(tabla)
    if tabla[indice][1] != catedra[1]:
        indice = rehash(tabla, indice)
    return indice
'PARA EJERCICIO 1'


'PARA EJERCICIO 5'
def insertar_contacto(t, contacto):
    indice = hash(contacto[0] + contacto[1])
    indice = indice % len(t)
    if t[indice] is None:
        t[indice] = contacto
    else:
        indice = rehash(t, indice)
        if t[indice] is None:
            t[indice] = contacto
'PARA EJERCICIO 5'
