from tdaarbol import NodoArbol, busqueda, eliminar, inorden
from tdaarbol import postorden, preorden, insertar, reemplazar

r = None
r = insertar(r, 4)
r = insertar(r, 6)
r = insertar(r, 3)
r = insertar(r, 10)
inorden(r)
print('aca')
preorden(r)
