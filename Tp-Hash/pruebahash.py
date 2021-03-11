from hash import crear_tabla_abierta, insert_palabra, barrido_abierta
from hash import busq_palabra, eliminar_palabra, telefono
from hash import crear_tabla_cerrada, rehash, nueva_catedra, barrido_cerrada
from hash import busq_catedra, docente, hash_1, insertar_contacto
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

#a. cargar catedras de una carrera de las cuales se conoce nombre, modalidad cantidad de horas
#b. ademas se deben poder agregar los docentes vinculados con las catedras
#c. debe ser una tabla cerrada
#d. debe poder solucionar las colisiones
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

#Ej 4 - Desarrollar un algoritmo que implemente una tabla hash cerrada para cargar personajes
# de Star Wars de los que solo se conoce su nombre

#a. la tabla inicialmente sera de 20 posiciones
#b. debera permitir el manejo de colisiones
#c. cuando el factor de carga de la tabla exceda el 75%, se debera incrementar el tamanio de la tabla al doble

'''
def carga(t):
    f = 0
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

    if carga(t) > 75:
        t = agrandarTabla(t)

    return t


t = crear_tabla_cerrada(20)

for i in range(0,15):
    t = insert_perj(t, random.choice(string.ascii_uppercase))

print(len(t)) #Hasta aca tiene 20 posiciones la tabla


t = insert_perj(t, random.choice(string.ascii_uppercase))

print(len(t)) #Se duplico el tamanio
'''



#Ej 5 - Desarrollar un algoritmo que implemente una tabla hash cerrada para administrar los
#contactos de personas de las cuales se conoce nombre, apellido y correo electronico,
#contemplando las siguientes pautas:

#a. El campo clave para generar las posiciones son el apellido y nombre.
#b. Debera contemplar una funcion de sondeo para resolver las colisiones.

'''
t = crear_tabla_cerrada(20)

for i in range(0,10):
    nombre = random.choice(string.ascii_uppercase)
    apellido = random.choice(string.ascii_lowercase)
    correo = random.randint(1, 100)
    contact = [nombre, apellido, correo]
    insertar_contacto(t, contact)

barrido_cerrada(t)
'''


#Ej 6 -
'''
legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']
legion = ''
num = ''
def codigo():
    legion = random.choice(legiones)
    num = random.randint(0000, 9999)
    codigo = legion + '-' + num
    return codigo

def insertar_codigo(t, codigo):
    legion, num = codigo.split('-')
    indice = hash(legion)
    indice = indice % len(t)
    insertar(t[indice], codigo)

def hash(codigo):
    legion, num = codigo.split("-")
    return (legion + num)

t = crear_tabla_abierta(10)
for i in range(0, 10):
    insertar_codigo(t, codigo)
barrido_abierta(t)
'''


#Ej 7 -
t_tipo = crear_tabla_cerrada(30)
t_pokemon = crear_tabla_abierta(15)
tipos = ['fuego', 'agua', 'planta', 'normal', 'electrico', 'hielo',
        'lucha', 'veneno', 'tierra', 'volador']

def pokemon(numero=0):
    numero = numero
    nombre = 'Nombre ' + [i]
    canttipo = random.randint(1,2)
    tipo = random.choice(tipos)

    if canttipo == 2:
        tipo += '-' + random.choice(tipos)

    nivel = random.randint(1,100)

    return [numero, nombre, tipo, nivel]
