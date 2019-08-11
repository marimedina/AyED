from tdalista import cargaAuto, insertar, eliminar, barrido
from tdalista import lista_vacia, tamanio, busqueda, Lista
from tdalista import cargaString
l1 = Lista()
l2 = Lista()
l3 = Lista()


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
cargaAuto(l1, 10)
barrido(l1)
aux = l1.inicio
aux1 = l1.inicio
while aux is not None:
    if aux.info % 2 == 0:
        insertar(l2, aux)
        aux1 = aux.sig
    else:
        insertar(l3, aux)
        aux1 = aux.sig
print('Lista de numeros pares:')
barrido(l2)
print('Lista de numeros impares:')
barrido(l3)
