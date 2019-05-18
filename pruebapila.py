from tdapila import apilar, desapilar, pila_llena, pila_vacia, tamanio, cima
from tdapila import Pila, cargautomatica, barrido, invertir, randString
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
'''cargautomatica(p)
print(p.datos)
barrido(p)
print(p.datos)'''


# ej1
'''cargautomatica(p)
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
print(p.datos)'''


#ej2 PREGUNTAR SI ESTA BIEN QUE APAREZCA NONE EN LOS NUMEROS ELIMINADOS
'''cargautomatica(p)
print(p.datos)
while not pila_vacia(p):
    aux = desapilar(p)
    if aux % 2 == 0:
        apilar(pp, aux)
    else:
        aux
print(pp.datos)'''


# ej3
'''cargautomatica(p)
print(p.datos)
paux = Pila()
num = 5
reemplazo = 2
while not pila_vacia(p):
    dato = desapilar(p)
    if dato == num:
        dato = reemplazo
    apilar(paux, dato)
while not pila_vacia(paux):
    apilar(p, desapilar(paux))
print(p.datos)'''


# ej4
'''cargautomatica(p)
print(p.datos)
paux = Pila()
while not pila_vacia(p):
    dato = desapilar(p)
    apilar(paux, dato)
print(paux.datos)'''


# ej5
'''palab = 'neuquen'
for elemento in palab:
    apilar(p, elemento)
print(palab)
while not pila_vacia(p):
    dato = desapilar(p)
    apilar(p1, dato)
    apilar(p2, dato)
invertir(p2, p)
print(p.datos)
print(p1.datos)
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
    print('No palindromo')'''


# ej6
'''palabra = 'Algoritmos'
for elemento in palabra:
    apilar(p, elemento)
print(palabra)

while not pila_vacia(p):
    invertir(p, p1)
print(p1.datos)
'''

# ej7
'''cargautomatica(p)
print(p.datos)
i = 5
while not pila_vacia(p):
    aux = desapilar(p)
    if i != p.tope + 1:
        apilar(p1, aux)
while not pila_vacia(p1):
    apilar(p, desapilar(p1))

barrido(p)'''


# ej8'
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
# parte A
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
print(p0.datos)
print(p1.datos)
print(p2.datos)
print(p3.datos)
# parte B
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
print(pi.datos)'''


# ej9


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


# ej12  QUEDA COLGADO
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


# ej14
num = '0123456789'
parrafo = 'Hoy, en mi casa hay 3 perros.'
voc = 'aeiouAEIOU'
cons = 'bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ'
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
print('Cantidad de espacios: ' + str(c_espacios)

# Parte C
c_total = (tamanio(p1) + tamanio(p2) + tamanio(p3))
por_voc = (tamanio(p1) * 100) / c_total
por_con = (tamanio(p2) * 100) / c_total
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
    if dat == 'z' or dat == 'Z'
        print('Existe al menos una z en el parrafo')
    else:
        print('No existe una z en el parrafo')


# ej19
'''while not pila_llena(p):'''
    '''largo = random.randint(1, 15)
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
