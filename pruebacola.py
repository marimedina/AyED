from tdacola import cargautomatica1, cola_llena, cola_vacia, arribo, atencion
from tdacola import Cola, mover_al_final, barridoc, cargaAutoStr
from tdacola import cargacaract, primo, tamanioc
from tdapila import invertir, apilar, Pila, desapilar, pila_vacia
from tdapila import cargautomatica, listaRandom
import random
import time
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

# ej4
'''cargautomatica1(c)
barridoc(c)
while not cola_vacia(c):
    aux = atencion(c)
    if primo(aux) is True:
        arribo(c1, aux)
print('Cola de numeros primos:')
barridoc(c1)'''


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
for i in range(0, c.tamanio):
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


# ej8
'''cargautomatica1(c)
barridoc(c)
num = 6
while not cola_vacia(c) and (c.frente < num):
    aux = atencion(c)
    arribo(c1, aux)
arribo(c1, num)
while not cola_vacia(c):
    aux = atencion(c)
    arribo(c1, aux)
c, c1 = c1, c
print('Cola con nuevo numero:')
barridoc(c)'''


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


# ej10
'''n = 6
s = 0
arribo(c, 0)
arribo(c, 1)
if n > 1:
    while tamanioc(c) < n:
        while tamanioc(c) > 2:
            arribo(c1, atencion(c))
        d1 = atencion(c)
        d2 = atencion(c)
        s = d1 + d2
        arribo(c1, d1)
        arribo(c1, d2)
        arribo(c1, s)
        c, c1 = c1, c
barridoc(c)'''


# ej11 ARREGLAR
'''c = 10
for i in range(1, c + 1):
    arribo(c1, (i*2))
print('Cola 1:')
barridoc(c1)
for i in range(1, c + 1):
    arribo(c2, (i*4))
print('Cola 2:')
barridoc(c2)
# no anda de aca para abajo
while not cola_vacia(c1) and not cola_vacia(c2):
    if c1.frente > c2.frente:
        arribo(c, atencion(c2))
    else:
        arribo(c, atencion(c1))
print('Cola final')
barridoc(c)'''


# ej12
'''cargacaract(c)
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
print('Hay ' + str(cont) + ' letras en la segunda cola')'''


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
    arribo(c, aux)
while not cola_vacia(c3):
    dat = atencion(c3)
    sum1 = sum + dat
    arribo(c1, dat)
if sum > sum1:
    print('La segunda cola es la mayor')
else:
    print('La primera cola es la mayor')


# Parte E
mult2 = 0
multiplo2 = 0
mult3 = 0
multiplo3 = 0
while not cola_vacia(c):
    dato = atencion(c)
    if dato % 2 == 0:
        mult2 += 1
    else:
        if dato % 3 == 0:
            mult3 += 1
    arribo(c3, dato)

while not cola_vacia(c1):
    dato = atencion(c1)
    if dato % 2 == 0:
        multiplo2 += 1
    else:
        if dato % 3 == 0:
            multiplo3 += 1
    arribo(c4, dato)

if mult2 > 0 and mult3 > 0:
    if multiplo2 > 0 and multiplo3 > 0:
        print('Ambas colas tienen multiplo de 2 y 3')
    else:
        print('Solo una de las colas posee multiplos')

# Parte D
p1, p2 = 0, 0
while not cola_vacia(c3):
    aux = atencion(c3)
    primo(aux)
    if True:
        p1 += 1
    arribo(c, aux)
while not cola_vacia(c4):
    dat = atencion(c4)
    primo(dat)
    if True:
        p2 += 1
    arribo(c1, dat)
if p1 == p2:
    print('Ambas colas tienen la misma cantidad de numeros primos')
else:
    if p1 > p2:
        print('La cola 1 tiene mas cantidad de numeros primos')
    else:
        print('La cola 2 tiene mas cantidad de numeros primos')'''


# ej17
'''cant = 10
letra = "ABCDEF"
for i in range(0, cant):
    turno = str(random.choice(letra))
    for j in range(0, 3):
        turno += str(random.randint(0, 9))
    arribo(c, turno)
barridoc(c)
# Parte B
while not cola_vacia(c):
    turno = atencion(c)
    if turno[0] in ["A", "C", "F"]:
        arribo(c1, turno)
    else:
        arribo(c2, turno)
print('Cola de turnos que comienzan con A, C, F:')
barridoc(c1)
print('Cola de turnos que comienzan con B, D, E:')
barridoc(c2)
# Parte C
ca, cc, cf = 0, 0, 0
cb, cd, ce = 0, 0, 0
contador = 0
letra = 0
if tamanioc(c1) > tamanioc(c2):
    print('La cola 1 tiene mas cantidad de turnos')
    for i in range(0, tamanioc(c1)):
        turno = atencion(c1)
        if turno[0] == 'A':
            ca += 1
        elif turno[0] == 'C':
            cc += 1
        else:
            cf += 1
        arribo(c1, turno)
    contador = ca
    letra = "A"
    if contador < cc:
        contador = cc
        letra = "C"
    if contador < cf:
        contador = cf
        letra = "F"
    print('La mayor cantidad de turnos comienzan con la letra ' + str(letra))
else:
    print('La cola 2 tiene mas cantidad de turnos')
    for j in range(0, tamanioc(c2)):
        turno = atencion(c2)
        if turno[0] == 'B':
            cb += 1
        elif turno[0] == 'D':
            cd += 1
        else:
            ce += 1
        arribo(c2, turno)
    contador = cb
    letra = "B"
    if contador < cd:
        contador = cd
        letra = "D"
    if contador < ce:
        contador = ce
        letra = "E"
    print('La mayor cantidad de turnos comienzan con la letra '+ str(letra))'''


# ej19


# ej20
'''vehiculos = ['auto', 'camion', 'colectivo', 'camioneta', 'trafic']
peajes = [c1, c2, c3]
cant1, cant2, cant3 = 0, 0, 0
i = 0
for i in range(0, 10):
    cab = random.randint(1, 3)
    dato = random.choice(vehiculos)
    if cab == 1:
        arribo(c1, dato)
    elif cab == 2:
        arribo(c2, dato)
    else:
        arribo(c3, dato)

print("Cabina 1:")
barridoc(c1)
print("Cabina 2:")
barridoc(c2)
print("Cabina 3:")
barridoc(c3)

while (not cola_vacia(c1)) or (not cola_vacia(c2)) or (not cola_vacia(c3)):
    if not cola_vacia(c1):
        atencion(c1)
        cant1 += 1
    if not cola_vacia(c2):
        atencion(c2)
        cant2 += 1
    if not cola_vacia(c3):
        atencion(c3)
        cant3 += 1

cant_mayor = cant1
cab_mayor = 1

if cant_mayor < cant2:
    cant_mayor = cant2
    cab_mayor = 2
if cant_mayor < cant3:
    cant_mayor = cant3
    cab_mayor = 3

print("La cabina que mas dinero recaudo fue: " + str(cab_mayor))'''


# ej21 TERMINAR
'''cdes = Cola()
cate = Cola()
cargautomatica1(cdes) #va ordenada
cargautomatica1(cate)
tipo_v = ['personas', 'negocios', 'carga']
ta = [10, 5, 7]
ts = [5, 3, 9]
while not cola_vacia(cdes) or not cola_vacia(cate):
    if not cola_vacia(cdes):
        ha = time.strftime("%H:%M")
        dato = frente(cdes)
        if dato.hsalida <= ha or cola_vacia(cate):
            dato = atencion(cdes)
            if
                dato.hsalida = nuevo_hs
                arribo(cdes)
            else:
                time.sleep(td[tipo_v(dato.tipo)])
                #cargar
    else:
        if not cola_vacia(cate):
            dato = atencion(cate)
            time.sleep(ta[tipo_v(dato.tipo)])'''
            #cargar
