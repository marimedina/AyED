from tdalista import cargaAuto, insertar, eliminar, barrido
from tdalista import lista_vacia, tamanio, Lista, eliminarNodo
from tdalista import cargaString, insertar1, primo, busquedaLista
from tdalista import campos
import math
import string
import random
l1 = Lista()
l2 = Lista()
l3 = Lista()
l4 = Lista()

'''cargaAuto(l1, 5)
barrido(l1)
while l1.inicio is not None:
    eliminarNodo(l1)
    print('lista 1')
    barrido(l1)'''


# ej1
'''cargaAuto(l1, 10)
barrido(l1)
print('El tamanio es: ' + str(l1.tamanio))'''

# ej2
'''cargaString(l1, 10)
barrido(l1)
aux1 = l1.inicio
aux = l1.inicio
while aux is not None:
    if ((aux.info == 'a') or (aux.info == 'e') or (aux.info == 'i') or
    (aux.info == 'o') or (aux.info == 'u') or (aux.info == 'A') or
    (aux.info == 'E') or (aux.info == 'I') or (aux.info == 'O') or
    (aux.info == 'U')):
        eliminar(l1, aux.info)
    aux = aux.sig
print('lista sin vocales')
barrido(l1)'''


# ej3
'''cargaAuto(l1, 10)
barrido(l1)
aux = l1.inicio
while aux is not None:
    if aux.info % 2 == 0:
        insertar(l2, aux.info)
    else:
        insertar(l3, aux.info)
    aux = aux.sig
print('Lista de numeros pares:')
barrido(l2)
print('Lista de numeros impares:')
barrido(l3)'''


# ej4
'''cargaAuto(l1, 10)
barrido(l1)
insertar1(l1, 100, 3)
print("Lista con elemente agregado")
barrido(l1)'''

# ej5
'''cargaAuto(l1, 10)
barrido(l1)
print()
aux = l1.inicio
while aux is not None:
    if primo(aux.info):
        eliminar(l1, aux.info)
    aux = aux.sig
print('Lista sin numeros primos:')
barrido(l1)'''


# ej6


# ej7
'''cargaAuto(l1, 5)
cargaAuto(l2, 5)
print('lista 1')
barrido(l1)
print('lista 2')
barrido(l2)
aux = l1.inicio
aux1 = l2.inicio
c = 0
while aux is not None:
    if aux.info != aux1.info:
        insertar(l3, aux.info)
        insertar(l3, aux1.info)
    else:
        c += 1
    aux = aux.sig
    aux1 = aux1.sig
print('listas unidas')
barrido(l3)
print('Hay ' + str(c) + ' elementos repetidos')
while not lista_vacia(l3):
    eliminarNodo(l3)
    print('Menos un nodo')
    barrido(l3)'''


# ej8 TERMINAR
'''while tamanio(l1) < 10:
    aleatorio = random.randint(-999, 999)
    if busquedaLista(l1, aleatorio) is None:
        if primo(aleatorio):
            #rango con anterior y siguiente +14
                insertar(l1, aleatorio)
        else:
            if aleatorio mod 2 != 0:
                #anterior y siguiente pares
                    insertar(l1, aleatorio)
barrido(l1)'''


# ej 9 TERMINAR ULTIMA PARTE
'''artistas = ["Arctic monkeys", "The strokes", "Miles Kane", "Oasis",
            "Radiohead", "The killers", "Coldplay", "Kings of leon",
            "The kooks", "Kasabian", "Josh Homme", "Foo fighters"]
for i in range(0, 10):
    nom = 'Nombre: ' + str(random.randint(0, 50))
    artis = random.choice(artistas)
    dur = random.randint(60, 180)
    reprod = random.randint(200, 1000)
    cancion = [nom, artis, dur, reprod]
    campos(l1, cancion, 1)
barrido(l1)
aux = l1.inicio
clarga = aux
while aux is not None:
    if (aux.info[2] > clarga.info[2]):
        clarga = aux
    aux = aux.sig
print('La cancion mas larga es ' + str(clarga.info))

# puedo ordenar de mayor a menor por reproducciones
# y mostrar los primeros 5/10/50
# No anda
aux = l1.inicio
aux1 = l2.inicio
while aux is not None:
    if aux.info[1] == 'Arctic monkeys':
        insertar(l2, aux)
    aux = aux.sig

if aux1 is None:
    print('No hay canciones de Arctic Monkeys')
else:
    print('Canciones de Arctic Monkeys')
    barrido(l2)'''


# ej10 ARREGLAR insertar

personajes = ['rey', 'darth vader', 'luke', 'leia', 'han solo', 'yoda',
              'chewbacca', 'grievous']
gen = ['Femenino', 'Masculino']
for i in range(0, 10):
    nombre = random.choice(personajes)
    altura = random.randint(100, 300)
    edad = random.randint(0, 60)
    genero = random.choice(gen)
    especie = random.choice(string.ascii_letters)
    planeta = random.choice(string.ascii_letters)
    episodio = random.randint(1, 9)
    pers = [nombre, altura, edad, genero, especie, planeta, episodio]
    insertar(l1, pers)
barrido(l1)

# Parte A
'''print('Lista de personajes femeninos')
aux = l1.inicio
while aux is not None:
    if aux.info[3] == 'Femenino':
        insertar(l2, aux.info)
    aux = aux.sig
barrido(l2)

# Parte B
d = 'Droide'
D = 'Droide'
print('Personajes de especie droide:')
aux = l1.inicio
while aux is not None:
    if aux.info[4] == 'd' or aux.info[4] == 'D':
        if (aux.info[6] == 1 or aux.info[6] == 2 or aux.info[6] == 3 or
        aux.info[6] == 4 or aux.info[6] == 5 or aux.info[6] == 6):
            insertar(l3, aux.info)
    aux = aux.sig
barrido(l3)

# Parte C
print('Informacion de Darth Vader')
aux = l1.inicio
while aux is not None:
    if aux.info[0] == 'darth vader':
        insertar(l4, aux.info)
    aux = aux.sig
barrido(l4)'''



# ej12 LISTA DOBLEMENTE ENLAZADA
