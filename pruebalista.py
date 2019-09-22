from tdalista import cargaAuto, insertar, eliminar, barrido
from tdalista import lista_vacia, tamanio, Lista, eliminarNodo
from tdalista import cargaString, insertar1, primo, busquedaLista
from tdalista import campos
import math
import random
l1 = Lista()
l2 = Lista()
l3 = Lista()

'''cargaAuto(l1, 5)
barrido(l1)
while l1.inicio is not None:
    eliminarNodo(l1)
    print('l1')
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


# ej 9
for i in range(0, 10):
    nom = 'Nombre: ' + str(random.randint(0, 50))
    artis = chr(65+i)
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


# ej12 LISTA DOBLEMENTE ENLAZADA
