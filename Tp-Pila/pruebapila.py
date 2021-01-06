from tdapila import apilar, desapilar, pila_llena, pila_vacia, tamanio, cima
from tdapila import Pila, cargautomatica, barrido, invertir, randString
from tdapila import quicksortI, listaRandom, dirrecionAnum, numAdirrecion
from tdapila import ordencre
import string
import random
p = Pila()
pp = Pila()
pi = Pila()
p0 = Pila()
p1 = Pila()
p2 = Pila()
p3 = Pila()


# pruebadebarrido
'''
cargautomatica(p)
print(p.datos)
invertir(p, p1)
print(p1.datos)
'''

# ej1 - Determinar el numero de ocurrencias de un determinado elemento en la pila
'''
cargautomatica(p)
print(p.datos)
paux = Pila()
num = 5
cont = 0
while not pila_vacia(p):
    dato = desapilar(p)
    if dato == num:
        cont += 1
    apilar(paux, dato)
print('Cantidad de ocurrencias:', cont)
while not pila_vacia(paux):
    apilar(p, desapilar(paux))
'''


# ej2 - Eliminar de una pila todos los elementos impares
'''
cargautomatica(p)
print(p.datos)
while not pila_vacia(p):
    aux = desapilar(p)
    if aux % 2 == 0:
        apilar(pp, aux)
    else:
        aux
print(pp.datos)
'''

# ej3 - Reemplazar todas las ocurrencias de un determinado elemento en una pila.
'''
cargautomatica(p)
print(p.datos)
paux = Pila()
num = 5 #numero a reemplazar
reemplazo = 2 #numero por el que se reemplaza
while not pila_vacia(p):
    dato = desapilar(p)
    if dato == num:
        dato = reemplazo
    apilar(paux, dato)
while not pila_vacia(paux):
    apilar(p, desapilar(paux))
print(p.datos)
'''

# ej4 - Invertir el contenido de una pila
'''
cargautomatica(p)
print(p.datos)
paux = Pila()
while not pila_vacia(p):
    dato = desapilar(p)
    apilar(paux, dato)
print(paux.datos)
'''


# ej5 - Determinar si una cadena de caracteres es un palindromo.
'''
palab = 'oso'
for elemento in palab:
    apilar(p, elemento)
print(palab)
while not pila_vacia(p):
    dato = desapilar(p)
    apilar(p1, dato)
    apilar(p2, dato)
invertir(p2, p)
# para abajo esta MAL
flag = True
while not pila_vacia(p):
    aux = desapilar(p)
    dat = desapilar(p1)
    apilar(p2, dat)
    if aux != dat:
        flag = False
if flag:
    print('Palindromo')
else:
    print('No palindromo')
'''


# ej6 - Leer una palabra y visualizarla en forma inversa.
'''
palabra = 'Algoritmos'
for elemento in palabra:
    apilar(p, elemento)
print(palabra)
while not pila_vacia(p):
    invertir(p, p1)
print(p1.datos)
'''


# ej7 - Eliminar el i-esimo elemento debajo de la cima
# (lo reemplaza al final por otro numero)
'''
cargautomatica(p)
print(p.datos)
i = 5
while not pila_vacia(p):
    aux = desapilar(p)
    if i != p.tope + 1:
        apilar(p1, aux)
while not pila_vacia(p1):
    apilar(p, desapilar(p1))

print(p.datos)
'''


# ej8 - Dada una pila de elemento (numero, palo) que representa una carta de baraja espanola,
# generada de forma aleatoria, resolver los siguientes puntos:
'''
dat = [5, 2]
apilar(p, dat)
dat = [6, 3]
apilar(p, dat)
dat = [10, 0]
apilar(p, dat)
dat = [1, 1]
apilar(p, dat)
dat = [11, 1]
apilar(p, dat)
print(p.datos)

# parte A - Separar la pila mazo en cuatro pilas una por cada palo.
while not pila_vacia(p):
    aux = desapilar(p)
    if aux[1] == 0:
        apilar(p0, aux)
    if aux[1] == 1:
        apilar(p1, aux)
    if aux[1] == 2:
        apilar(p2, aux)
    if aux[1] == 3:
        apilar(p3, aux)
print('Palo 0:')
print(p0.datos)
print('Palo 1:')
print(p1.datos)
print('Palo 2:')
print(p2.datos)
print('Palo 3:')
print(p3.datos)

# parte B - Ordenar una de las cuatro pilas de manera creciente.
while not pila_vacia(p1):
    aux = desapilar(p1)
    if pila_vacia(pi):
        apilar(pi, aux)
    else:
        while not pila_vacia(pi) and aux < cima(pi):
            apilar(pp, desapilar(pi))
        apilar(pi, aux)
        while not pila_vacia(pp):
            apilar(pi, desapilar(pp))

print('Pila ordenada de manera creciente')
print(pi.datos)
'''


# ej9
fact = 1
num = 6
apilar(p, num)
while num > 0:
    apilar(p, num)
    num -= 1
while not pila_vacia(p):
    fact *= desapilar(p)
print(fact)


# ej10
'''cargautomatica(p)
print(p.datos)
while not pila_vacia(p):
    aux = desapilar(p)
    if aux % 2 == 0:
        apilar(pp, aux)
    else:
        apilar(pi, aux)
print('pila par')
print(pp.datos)
print('pila impar')
print(pi.datos)'''

# ej11
'''palabra = 'algoritmos'
cont = 0
for elemento in palabra:
    apilar(p, elemento)
print(p.datos)
while not pila_vacia(p):
    aux = desapilar(p)
    if aux == 'a' or aux == 'e' or aux == 'i' or aux == 'o' or aux == 'u':
        cont += 1
apilar(p1, aux)
print('Hay ' + str(cont) + ' vocales')'''


# ej12
'''num = int(input('Ingrese un numero: '))
while num != 0:
    if not pila_llena(p):
        while not pila_vacia(p) and (cima(p) >= num):
            apilar(p1, desapilar(p))
        apilar(p, num)
        while not pila_vacia(p1):
            apilar(p, desapilar(p1))
    else:
        print('Pila llena')
    barrido(p)
    num = int(input('Ingrese un numero: '))'''


# ej13
'''lista = listaRandom(25)
print(lista)
quicksortI(lista, 0, len(lista) - 1)
print(lista)'''


# ej14
'''num = '0123456789'
parrafo = 'Hoy, en mi casa hay 3 perros.'
voc = 'aeiouAEIOU'
cons = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
for elemento in parrafo:
    if elemento in voc:
        apilar(p1, elemento)
    else:
        if elemento in cons:
            apilar(p2, elemento)
        else:
            apilar(p3, elemento)
# Parte A
print('Cantidad de vocales: ' + str(tamanio(p1)))
print('Cantidad de consonantes: ' + str(tamanio(p2)))
print('Cantidad de signos o numeros: ' + str(tamanio(p3)))

# Parte B
c_espacios = 0
while not pila_vacia(p3):
    aux = desapilar(p3)
    if aux == ' ':
        c_espacios += 1
print('Cantidad de espacios: ' + str(c_espacios))

# Parte C
c_total = (tamanio(p1) + tamanio(p2) + tamanio(p3))
por_voc = (tamanio(p1) * 100) // c_total
por_con = (tamanio(p2) * 100) // c_total
print('Porcentaje de vocales: ' + str(por_voc))
print('Porcentaje de consonantes: ' + str(por_con))


# Parte D
c_numeros = 0
while not pila_vacia(p3):
    aux = desapilar(p3)
    if aux == num:
        c_numeros += 1
print('Cantidad de numeros: ' + str(c_numeros))


# Parte E
if tamanio(p1) == tamanio(p3):
    print('Tienen cantidades iguales')
else:
    print('No tienen cantidades iguales')


# Parte F
while not pila_vacia(p2):
    dat = desapilar(p3)
    if dat == 'z' or dat == 'Z':
        print('Existe al menos una z en el parrafo')
    else:
        print('No existe una z en el parrafo')'''


# ej15
'''cont = 8
obj = ['mouse', 'teclado', 'carpeta', 'cartuchera', 'perforadora',
       'abrochadora', 'escritorio', 'computadora']
for i in range(0, cont):
    objeto = random.choice(obj)
    peso = random.randint(0, 25)
    apilar(p, [objeto, peso])
p1 = ordencre(p)
barrido(p1)'''


# ej16
'''max = 10
movs = ['norte', 'sur', 'este', 'oeste', 'noreste', 'sureste',
        'noroeste', 'suroeste']
camino = []
camino_vuelta = []
for i in range(0, max):
    movimientos = random.choice(movs)
    camino.append(movimientos)
    apilar(p, dirrecionAnum(movimientos))
while not pila_vacia(p):
    n = 10 - desapilar(p)
    camino_vuelta.append(numAdirrecion(n))
print('recorrido:')
print(camino)
print('recorrido de vuelta:')
print(camino_vuelta)'''


# ej17
'''n = 5
apilar(p, 0)
if (n == 1):
    apilar(p, 1)
elif (n > 1):
    apilar(p, 1)
    while not pila_llena(p) and tamanio(p) <= n:
        dato = desapilar(p)
        dato1 = cima(p)
        apilar(p, dato)
        apilar(p, (dato + dato1))
barrido(p)'''

# ej18
'''cargautomatica(p)
print(p.datos)
prom = 0
med = 0
tempmin = cima(p)
tempmax = cima(p)
mayores = 0
menores = 0
while not pila_vacia(p):
    aux = desapilar(p)
    med = med + aux
    prom += 1
    if aux <= tempmin:
        tempmin = aux
    elif aux > tempmax:
        tempmax = aux
    apilar(p1, aux)
rang = tempmax - tempmin
media = med // prom
while not pila_vacia(p1):
    aux = desapilar(p1)
    if aux >= media:
        mayores += 1
    else:
        menores += 1
    apilar(p2, aux)

# Parte A
print('Temperatura minima: ' + str(tempmin))
print('Temperatura maxima: ' + str(tempmax))
print('Rango: ' + str(rang))

# Parte B
print('Promedio del total de valores: ' + str(media))

# Parte C
print('Valores por encima: ' + str(mayores))
print('Valores por debajoo iguales: ' + str(menores))'''

# ej19
'''while not pila_llena(p):
    largo = random.randint(1, 15)
    apilar(p, randString(largo))

while not pila_vacia(p):
    aux = desapilar(p)
    if len(aux) > 7:
        print(aux)
    apilar(p1, aux)
print(p1.datos)'''


# ej20 PARA ESTE CAMBIAR MAX Y RANDOM
'''cargautomatica(p)
print(p.datos)
while not pila_vacia(p):
    aux = desapilar(p)
    if aux % 2 == 0 or aux % 3 == 0 or aux % 5 == 0:
        apilar(p1, aux)
barrido(p1)'''
