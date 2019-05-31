from tdacola import cargautomatica1, cola_llena, cola_vacia, arribo, atencion
from tdacola import Cola, mover_al_final, barridoc, cargaAutoStr
from tdacola import cargacaract
from tdapila import invertir, apilar, Pila, desapilar, pila_vacia
from tdapila import cargautomatica, listaRandom
c = Cola()
c1 = Cola()
c2 = Cola()
c3 = Cola()
c4 = Cola()
p = Pila()
p1 = Pila()


# ejcarpeta
'''
cargautomatica1(c)
print(c.datos)
while not cola_vacia(c):
    aux = atencion(c)
    if aux % 2 == 0:
        arribo(c1, aux)
    else:
        arribo(c2, aux)
print(c1.datos)
print(c2.datos)
'''

# ej1
'''cargaAutoStr(c)
print(c.datos)
while not cola_vacia(c):
    aux = atencion(c)
    if not (aux == 'a' or aux == 'e' or aux == 'i' or aux == 'o' or aux == 'u'
    or aux == 'A' or aux == 'E' or aux == 'I' or aux == 'O' or aux == 'U'):
        arribo(c1, aux)
print(c1.datos)'''


# ej2
'''cargautomatica1(c)
print(c.datos)
while not cola_vacia(c):
    dato = atencion(c)
    apilar(p, dato)
while not pila_vacia(p):
    dat = desapilar(p)
    arribo(c1, dat)
print(c1.datos)'''


# ej3
'''palabra = 'casa'
for letra in palabra:
    arribo(c, letra)
    apilar(p, letra)
palindromo = True
while not cola_vacia(c):
    dato = atencion(c)
    if dato != desapilar(p):
        palindromo = False
    arribo(c1, dato)
if palindromo:
    print('es palindromo')
else:
    print('no es palindromo')'''

# ej4 MAL MAL MAL
'''cargautomatica1(c)
print(c.datos)
while not cola_vacia(c):
    aux = atencion(c)
    if aux < 2:
        arribo(c1, aux)
    else:
        if aux == 2:
            arribo(c1, aux)
        else:
            for i in range(2, aux):
                if (aux % i != 0) and (aux != i):
                    arribo(c1, aux)
print(c1.datos)'''


# ej5
'''cargautomatica1(c)
while not cola_vacia(c):
    dato = atencion(c)
    apilar(p, dato)
print(p.datos)
invertir(p, p1)
print(p1.datos)'''


# ej6
'''cargautomatica1(c)
barridoc(c)
num = 5
cont = 0
for i in range(0, tamanioc(c)):
    dato = atencion(c)
    if (dato == num):
        cont += 1
    arribo(c, dato)
print('cantidad de ocurrencias: ' + str(cont))'''


# ej7
'''cargautomatica1(c)
barridoc(c)
pos = 6
for i in range(0, tamanioc(c)):
    if i == pos:
        atencion(c)
    else:
        arribo(c1, atencion(c))
print('Cola sin elemento en posicion: ' + str(pos))
barridoc(c1)'''


# ej8 NO ANDAAAAAAAAAAAAAAAA
'''cargautomatica1(c)
print(c.datos)
num = 6
while not cola_vacia(c) and (c.frente < num):
    arribo(c1, atencion(c))
arribo(c1, num)
while not cola_vacia(c):
    arribo(c1, atencion(c))
print(c1.datos)'''


# ej9 PARA ESTE CAMBIAR CARGA AUTOMATICA (-50,50)
'''cargautomatica1(c)
barridoc(c)
min = c.frente
max = c.frente
cont = 0
while not cola_vacia(c):
    aux = atencion(c)
    if aux <= min:
        min = aux
    elif aux > max:
        max = aux
    arribo(c1, aux)
    if aux < 0:
        cont += 1
rango = max - min
print('rango: ' + str(rango))
print('cantidad de numero negativos: ' + str(cont))'''


# ej10 ARREGLARRRRRRRRRR
'''n = 5
arribo(c, 0)
if n == 1:
    arribo(c, 1)
elif n > 1:
    arribo(c, 1)
    while not cola_llena(c) and (c.tamanio <= n):
        aux = atencion(c)
        dato = c.final
        arribo(c, aux)
        arribo(c, (aux + dato))
barridoc(c)'''


# ej12
cargacaract(c)
print(c.datos)
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.;/*-+=%#!?"
# Parte A
while not cola_vacia(c):
    aux = atencion(c)
    for i in range(0, 21):
        if aux == i:
            arribo(c1, aux)
    for elemento in caracteres:
        if aux == elemento:
            arribo(c2, aux)
print(c1.datos)
print(c2.datos)

# Parte B
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
cont = 0
while not cola_vacia(c2):
    aux = atencion(c2)
    for elemento in letras:
        if aux == elemento:
            cont += 1
    arribo(c4, aux)
print('Hay ' + str(cont) + ' letras en la segunda cola')


# ej14
'''cargautomatica1(c)
print(c.datos)
cargautomatica1(c1)
print(c1.datos)
# Parte A
if c.tamanio == c1.tamanio:
    print('Ambas colas tienen la misma cantidad de elementos')
else:
    print('No poseen la misma cantidad de elementos')

# Parte B
iguales = False
while not cola_vacia(c):
    aux = atencion(c)
    while not cola_vacia(c1):
        dat = atencion(c1)
        if aux == dat:
            iguales = True
        else:
            iguales = False
        arribo(c3, dat)
    arribo(c4, aux)
if iguales:
    print('Colas iguales')
else:
    print('Colas distintas')

# Parte C
sum = 0
sum1 = 0
while not cola_vacia(c4):
    aux = atencion(c4)
    sum = sum + aux
while not cola_vacia(c3):
    dat = atencion(c3)
    sum1 = sum + dat
if sum < sum1:
    print('La primera cola es la mayor')
else:
    print('La segunda cola es la mayor')


# Parte E ARREGLAR
mult2 = False
multiplo2 = False
mult3 = False
multiplo2 = False
while not cola_vacia(c3) and not cola_vacia(c4):
    dato = atencion(c3)
    dato1 = atencion(c4)
    if dato % 2 == 0:
        mult2 = True
    elif dato1 % 2 == 0:
        multiplo2 = True
    arribo(c, dato)
    arribo(c1, dato1)

while not cola_vacia(c) and not cola_vacia(c1):
    dato = atencion(c)
    dato1 = atencion(c1)
    if dato % 3 == 0:
        mult3 = True
    elif dato1 % 3 == 0:
        multiplo3 = True
    arribo(c3, dato)
    arribo(c4, dato1)

if mult2 is True and multiplo2 is True:
    print('Ambas colas poseen al menos un multiplo de 2')
else:
    print('Ambas no poseen al menos un multiplo de 2')
if mult3 is True and multiplo3 is True:
    print('Ambas colas poseen al menos un multiplo de 3')
else:
    print('Ambas no poseen al menos un multiplo de 3')'''
