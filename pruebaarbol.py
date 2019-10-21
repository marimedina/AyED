from tdaarbol import NodoArbol, busqueda, eliminar, inorden
from tdaarbol import postorden, preorden, insertar, reemplazar
import random
'''r = None
r = insertar(r, 4)
r = insertar(r, 6)
r = insertar(r, 3)
r = insertar(r, 10)
inorden(r)
print('aca')
preorden(r)'''

# ej1 TERMINAR
'''r = None
for i in range(0, 10):
    r = insertar(r, random.randint(0, 100))
# Parte A
print('Barrido preorden:')
preorden(r)
print('Barrido inorden:')
inorden(r)
print('Barrido postorden:')
postorden(r)
# Parte B
n = 45
if busqueda(r, n) is None:
    print('El numero no se encuentra en el arbol')
else:
    print('EL numero se encuentra en el arbol')
# Parte C
for i in range(0, 2):
    eliminar(r, )'''


# ej5
r = None
"True heroe, false villano"
super = ["Ironman ", "Spiderman ", "CapitanAmerica ", "Dr.Strange ",
        "Hulk ", "BlackPanter "]
for elemento in super:
    r = insertar(r, random.choice(super) + str(random.choice([True, False])))
preorden(r)
# Parte D
