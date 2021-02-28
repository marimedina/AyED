from hash import crear_tabla_abierta, insert_palabra, barrido_abierta
from hash import busq_palabra, eliminar_palabra, telefono
from hash import crear_tabla_cerrada, rehash, nueva_catedra, barrido_cerrada
from hash import busq_catedra, docente, hash_1
from tdalista import *
import random
import string


# Ej 1 - Desarrollar un algoritmo que permita implementar una tabla hash para representar un
# diccionario que permita resolver:
'''
t = crear_tabla_abierta(28)

# Parte A - agregar una palabra y su significado al diccionario
print('Dicc con palabras agregadas:')
insert_palabra(t, 'pesa', 'mancuerna para ejercitar')
insert_palabra(t, 'casa', 'construccion destinada a ser habitada')
insert_palabra(t, 'ventana', 'abertura que brinda iluminacion y ventilacion')
barrido_abierta(t)


# Parte B - determinar si una palabra existe y mostrar su significado
print('')
aux = busq_palabra(t, 'casa')
if aux is not None:
    print('La palabra fue encontrada ' + str(aux.info))
else:
    print('La palabra no se encontro')


# Parte C - borrar una palabra del diccionario
print('')
eliminar_palabra(t, 'casa')
print('Tabla sin palabra casa:')
barrido_abierta(t)
'''


#Ej 2 - Desarrollar un algoritmo que implemente una tabla hash para una guia de telefono, los
# datos que se conocen son numero de telefono, apellido, nombre y direccion de la persona.
# El campo clave debe ser el numero de telufono.
'''
t = crear_tabla_abierta(20)

def hash(telefono):
    area, num = telefono.split("-")
    area = int(area)
    num = int(num)
    return (area + num)


def insert_tel(tabla, telefono, nom_apellido, direccion):
    indice = hash(telefono) % len(tabla)
    campos(tabla[indice], [telefono, nom_apellido, direccion], 0)


for i in range(0, 25):
    insert_tel(t, telefono(), 'Nombre ' + random.choice(string.ascii_uppercase),
              'Direccion ' + random.choice(string.ascii_lowercase))

print('Guia telefonica:')
barrido_abierta(t)

print('')
for i in range(0, len(t)):
    if t[i].tamanio > 0:
        print('En el indice ' + str(i) + ' hay ' + str(t[i]. tamanio) + ' numeros')
'''


#Ej 3 - Implementar un tabla hash cerrada para guardar las catedras de una carrera universitaria
# de acuerdo a su codigo
'''
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



for i in range(0, 10):
    catedra = nueva_catedra()
    cargar_catedra(t, catedra)
barrido_cerrada(t)
'''

#Ej 4

def carga(t):
    'Para controlar el factor de carga de la tabla'
    ocupados = 0
    for personaje in t:
        if personaje is not None:
            ocupados += 1
    f = (ocupados*100) / len(t)
    return f

def agrandarTabla(t):
    t1 = crear_tabla_cerrada(len(t)*2)
    for personaje in t:
        if personaje is not None:
            insert_perj(t1, personaje)
    return t1

def insert_perj(t, personaje):
    indice = hash_1(personaje)
    indice = indice % len(t)

    if t[indice] is not None:
        indice = rehash(t, indice)
    t[indice] = personaje

    if f > 75:
        t = agrandarTabla(t)
    return t
