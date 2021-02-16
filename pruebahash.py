from hash import crear_tabla_abierta, insert_palabra, barrido_abierta
from hash import busq_palabra, eliminar_palabra, telefono, insertar_por_campo
from hash import crear_tabla_cerrada, rehash, nueva_catedra, barrido_cerrada
from hash import busq_catedra, docente, hash_1
from tdalista import *
import random
import string
# ej 1
'''t = crear_tabla_abierta(28)
# Parte A
insert_palabra(t, 'pesa', 'mancuerna para ejercitar')
insert_palabra(t, 'casa', 'construccion destinada a ser habitada')
insert_palabra(t, 'ventana', 'abertura que brinda iluminacion y ventilacion')
barrido_abierta(t)
# Parte B
aux = busq_palabra(t, 'casa')
if aux is not None:
    print('La palabra fue encontrada ' + str(aux.info))
else:
    print('La palabra no se encontro')
# Parte C
eliminar_palabra(t, 'casa')
print('Tabla sin palabra casa:')
barrido_abierta(t)'''


# ej 2
'''t = crear_tabla_abierta(20)


def hash(telefono):
    area, num = telefono.split("-")
    area = int(area)
    num = int(num)
    return (area + num)


def insert_tel(tabla, telefono, nom_apellido, direccion):
    indice = hash(telefono) % len(tabla)
    insertar_por_campo(tabla[indice], [telefono, nom_apellido, direccion], 0)


for i in range(0, 25):
    insert_tel(t, telefono(), 'Nombre ' + random.choice(string.ascii_uppercase),
              'Direccion ' + random.choice(string.ascii_lowercase))
print('Guia telefonica')
barrido_abierta(t)
for i in range(0, len(t)):
    if t[i].tamanio > 0:
        print('En el indice ' + str(i) + ' hay ' + str(t[i]. tamanio) + ' numeros')'''

# ej 3 FIJARSE PORQUE SALE UNA POSICION DE MAS
t = crear_tabla_cerrada(20)


def cargar_catedra(t, dato):
    clave = hash(dato[0])
    indice = clave % len(t)
    if t[indice] is None:
        t[indice] = dato
    else:
        indice = rehash(t, indice)
        if indice is not None:
            t[indice] = dato
        else:
            print("No hay lugar en la tabla")


'''cantidad a insertar es 20'''
for i in range(0, 20):
    catedra = nueva_catedra()
    cargar_catedra(t, catedra)
barrido_cerrada(t)


# ej 4
#def insert_perj(t, personaje):
#    indice = hash_1(personaje)
