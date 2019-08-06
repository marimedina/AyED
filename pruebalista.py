from tdalista import cargaAuto, insertar, eliminar, barrido
from tdalista import lista_vacia, tamanio, busqueda, Lista
from tdalista import cargaString
l1 = Lista()

# ej1
'''cargaAuto(l1, 10)
barrido(l1)
print('El tamanio es: ' + str(l1.tamanio))'''

# ej2
cargaString(l1, 10)
barrido(l1)
aux1 = l1.inicio
aux = l1.inicio
while aux is not None:
    if ((aux == 'a') or (aux == 'e') or (aux == 'i') or (aux == 'o')
    or (aux == 'u') or (aux == 'A') or (aux == 'E') or (aux == 'I')
    or (aux == 'O') or (aux == 'U')):
        eliminar(l1, aux)
        aux = l1.inicio
print('aca')
barrido(l1)
