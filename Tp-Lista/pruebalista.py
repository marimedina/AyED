from tdalista import cargaAuto, insertar, eliminar, barrido
from tdalista import lista_vacia, tamanio, Lista, eliminarNodo
from tdalista import cargaString, insertar1, primo, busquedaLista
from tdalista import campos, finLista
from tdalistaenlazada import insertar2, Lista2, barrido2, busquedacampos2
from tdalistaenlazada import campos2, tamanio2
import math
import string
import random
import calendar
import datetime
l1 = Lista()
l2 = Lista()
l3 = Lista()
l4 = Lista()
l5 = Lista()
l6 = Lista()

# NO ANDAN/FALTAN:
# 8 SE CUELGA

'''cargaAuto(l1, 5)
barrido(l1)
while l1.inicio is not None:
    eliminarNodo(l1)
    print('lista 1')
    barrido(l1)'''


# ej1 - Algoritmo que cuente la cantidad de nodos de una lista.
'''
cargaAuto(l1, 5)
barrido(l1)
print('El tamanio es: ' + str(l1.tamanio))
'''


# ej2 - Algoritmo que elimina las vocales de una lista de caracteres.
'''
cargaString(l1, 10)
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
print('Lista sin vocales:')
barrido(l1)
'''


# ej3 - Dada una lista de numeros enteros, implementar un algoritmo que la divida en dos, una
# con los numeros pares y otra con los numeros impares.
'''
cargaAuto(l1, 10)
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
barrido(l3)
'''


# ej4 - algoritmo que inserte un nodo en la i-esima posicion de una lista.
'''
cargaAuto(l1, 10)
barrido(l1)
insertar1(l1, 100, 3)
print("Lista con elemente agregado")
barrido(l1)
'''

# ej5 - Dada una lista de numeros enteros eliminar de estas los primos.
'''
cargaAuto(l1, 10)
barrido(l1)
aux = l1.inicio
while aux is not None:
    if primo(aux.info):
        eliminar(l1, aux.info)
    aux = aux.sig
print('Lista sin numeros primos:')
barrido(l1)
'''


# ej6 - Dada una lista con el siguiente tipo de registro, superheroe (nombre aparicion, casa, biografia)
'''
sheroes = ['Linterna Verde', 'Wolverine', 'Ant Man', 'Ironman', 'Black Panter']
casas = ['Marvel', 'DC']
bio = ['traje', 'garras', 'armadura', 'nada', 'mascara']
for i in range(0, 6):
    nombre = random.choice(sheroes)
    aparicion = random.randint(1000, 2000)
    casa = random.choice(casas)
    biografia = random.choice(bio)
    super = [nombre, aparicion, casa, biografia]
    campos(l1, super, 0)
barrido(l1)

# Parte A - Eliminar el nodo que contiene la informacion de Linterna Verde.
aux = l1.inicio
while aux is not None:
    if aux.info[0] == 'Linterna Verde':
        eliminar(l1, aux.info)
    aux = aux.sig
print('A - Lista sin linterna verde:')
barrido(l1)

# Parte B - Mostrar el anio de aparicion de Wolverine.
aux = l1.inicio
print('B - Aparicion de Wolverine:')
while aux is not None:
    if aux.info[0] == 'Wolverine':
        print(aux.info[1])
    aux = aux.sig

# Parte C - Cambiar la casa de Ant-Man a Marvel.
aux = l1.inicio
while aux is not None:
    if aux.info[0] == 'Ant Man':
        aux.info[2] = 'Marvel'
    aux = aux.sig
print('C - cambiar casa de ant-man')
barrido(l1)

# Parte D - Mostrar el nombre de aquellos que en su biografia menciona lapalabra traje o armadura.
print('D - Aquellos con traje o armadura')
aux = l1.inicio
while aux is not None:
    if aux.info[3] == 'traje' or aux.info[3] == 'armadura':
        print(aux.info[0])
    aux = aux.sig

# Parte E - Mostrar el nombre y la casa, cuya fecha de aparicion sea anterior a 1963.
print('F - Nombre y casa de heroes con anio de aparecion menor a 1963')
aux = l1.inicio
while aux is not None:
    if aux.info[1] < 1963:
        print(aux.info[0] + ' ' + aux.info[2])
    aux = aux.sig
'''


# ej7 - Escribir un algoritmo que realice las siguientes actividades:
'''
cargaAuto(l1, 4)
cargaAuto(l2, 4)
print('Lista 1:')
barrido(l1)
print('Lista 2:')
barrido(l2)

#hago una copia de l1 para los sig ejercicios
copl1 = Lista()
au = l1.inicio
while au is not None:
    insertar(copl1, au.info)
    au = au.sig


#Parte A - Concatenar dos listas una atras de otra
print('A - Listas concatenadas')
aux = finLista(l1)
aux.sig = l2.inicio
barrido(l1)


#Parte B - Concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden.
aux = l1.inicio
while aux is not None:
    if busquedaLista(l3, aux.info) is None:
        insertar(l3, aux.info)
    aux = aux.sig

print('B - Lista sin datos repetidos y ordenados')
barrido(l3)


#Parte C - Contar cuantos elementos repetidos hay entre dos listas (es decir su interseccion).
aux = copl1.inicio
cont = 0
print('C - Cantidad de elementos repetidos entre ambas listas:')
while aux is not None:
    if (busquedaLista(l2, aux.info) is not None) and (busquedaLista(l4, aux.info) is None):
        cont += 1
    aux = aux.sig
print(cont)


#Parte D - Eliminar todos los nodos de una lista de a uno a la vez.
print('Parte D')
while not lista_vacia(l3):
    eliminarNodo(l3)
    print('--')
    barrido(l3)
'''



# ej8 TERMINAR - SE CUELGA
'''
while tamanio(l1) < 5:
    aleat = random.randint(0, 15) #Parte A - poner -999 a +999
    if l1.tamanio == 0:
        insertar(l1, aleat)
    else:
        if busquedaLista(l1, aleat) is None:
            if l1.tamanio == 1:
                if (primo(aleat)) and (abs(l1.inicio.info - aleat) > 14): #Parte C
                    insertar(l1, aleat)
                else:
                    if ((aleat % 2) != 0) and ((l1.inicio.info % 2) == 0) and (not primo(aleat)): #Parte D
                        insertar(l1, aleat)
            else:
                ant = l1.inicio
                sig = ant.sig
                while (sig is not None) and (sig.info < aleat):
                    if (primo(aleat)) and (abs(ant.info - aleat) < 14):
                        insertar(l1, aleat)
                    else:
                        if ((aleat % 2) != 0) and ((ant.info % 2) == 0) and (not primo(aleat)):
                            insertar(l1, aleat)
barrido(l1)
'''

# ej 9 TERMINAR PARTE B
artistas = ["Arctic monkeys", "The strokes", "Miles Kane", "Oasis",
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

# Parte A
'''aux = l1.inicio
clarga = aux
while aux is not None:
    if (aux.info[2] > clarga.info[2]):
        clarga = aux
    aux = aux.sig
print('La cancion mas larga es ' + str(clarga.info))'''

# Parte B mal
# puedo ordenar de mayor a menor por reproducciones
# y mostrar los primeros 5/10/50

# Parte C
'''aux = l1.inicio
while aux is not None:
    if aux.info[1] == 'Arctic monkeys':
        insertar(l2, aux.info)
    aux = aux.sig
print('Canciones de Arctic Monkeys')
barrido(l2)'''


# ej10
'''personajes = ['rey', 'darth vader', 'luke', 'leia', 'han solo', 'yoda',
              'chewbacca', 'grievous']
gen = ['Femenino', 'Masculino']
esp = ['humano', 'droide', 'wookies', 'ewoks', 'gungan', 'jawas']
pla = ['naboo', 'ender', 'kashyyyk', 'tatooine', 'coruscant', 'alderan']
for i in range(0, 10):
    nombre = random.choice(personajes)
    altura = random.randint(50, 200)
    edad = random.randint(400, 1500)
    genero = random.choice(gen)
    especie = random.choice(esp)
    planeta = random.choice(pla)
    episodio = random.randint(1, 9)
    pers = [nombre, altura, edad, genero, especie, planeta, episodio]
    insertar(l1, pers)
barrido(l1)'''

# Parte A
'''print('Lista de personajes femeninos')
aux = l1.inicio
while aux is not None:
    if aux.info[3] == 'Femenino':
        insertar(l2, aux.info)
    aux = aux.sig
barrido(l2)'''

# Parte B
'''print('Personajes de especie droide:')
aux = l1.inicio
while aux is not None:
    if aux.info[4] == 'droide':
        if (aux.info[6] == 1 or aux.info[6] == 2 or aux.info[6] == 3 or
        aux.info[6] == 4 or aux.info[6] == 5 or aux.info[6] == 6):
            insertar(l3, aux.info)
    aux = aux.sig
barrido(l3)'''

# Parte C
'''print('Informacion de Darth Vader')
aux = l1.inicio
while aux is not None:
    if aux.info[0] == 'darth vader':
        insertar(l4, aux.info)
    aux = aux.sig
barrido(l4)'''

# Parte D
'''print('Personajes del episodio 4 al 7')
aux = l1.inicio
while aux is not None:
    if (aux.info[6] == 4 or aux.info[6] == 5 or aux.info[6] == 6 or
       aux.info[6] == 7):
        insertar(l5, aux.info)
    aux = aux.sig
barrido(l5)'''

# Parte E
'''print('Personajes mayores a 850 anios')
aux = l1.inicio
while aux is not None:
    if aux.info[2] > 850:
        print(aux.info)
        insertar(l6, aux.info)
    aux = aux.sig

dat = l6.inicio
mayor = dat
while dat is not None:
    if dat.info[2] > mayor.info[2]:
        mayor = dat
    dat = dat.sig
print('El personaje de mayor edad es:')
print(mayor.info)'''

# Parte F
'''aux = l1.inicio
print('Sin personajes de episodios 4, 5 y 6')
while aux is not None:
    if aux.info[6] == 4 or aux.info[6] == 5 or aux.info[6] == 6:
        eliminar(l1, aux.info)
    aux = aux.sig
barrido(l1)'''

# Parte G
'''aux = l1.inicio
while aux is not None:
    if aux.info[4] == 'humano':
        if aux.info[5] == 'alderan':
            insertar(l3, aux.info)
    aux = aux.sig
print('Personajes humanos de Alderan')
barrido(l3)'''

# Parte H
'''print('Personajes con menos de 70 centimetros')
aux = l1.inicio
while aux is not None:
    if aux.info[1] < 70:
        print(aux.info)
    aux = aux.sig'''

# Parte I
'''aux = l1.inicio
while aux.sig.sig is not None:
    aux = aux.sig
eliminar(l1, aux.info)
print('Lista sin el ante ultimo elemento')
barrido(l1)'''

# Parte J
'''print('Chewbacca')
aux = l1.inicio
while aux is not None:
    if aux.info[0] == 'chewbacca':
        insertar(l4, aux.info[6])
    aux = aux.sig
print('Aparece en los episodios:')
barrido(l4)'''

# ej12

# ej13

# ej14 FALTA PARTE D, H
'''l1 = Lista2()
pokemons = ['Bulbasaur', 'Ivysaur', 'Charmander', 'Squirtle', 'Caterpie']
tipos = ['fuego', 'agua', 'planta', 'bicho', 'volador', 'veneno', 'electrico']
entrenadores = ['Pepito', 'Mariana', 'Pedro', 'Jose', 'Alicia', 'Luciano']
for i in range(0, 6):
    nombre = entrenadores[i]
    t_ganados = random.randint(0, 10)
    b_perdidas = random.randint(0, 10)
    b_ganadas = random.randint(0, 10)
    entr = [nombre, t_ganados, b_perdidas, b_ganadas]
    campos2(l1, entr, 0)
    nodo = busquedacampos2(l1, entr[0], 0)
    laux = nodo.lista
    for j in range(0, 3):
        nomb = random.choice(pokemons)
        nivel = random.randint(1, 40)
        tipo = random.choice(tipos)
        subtipo = random.choice(string.ascii_uppercase)
        pok = [nomb, nivel, tipo, subtipo]
        campos2(laux, pok, 0)
barrido2(l1)'''

# Parte A
'''print('Cantidad de pokemons por jugador: ' + str(tamanio2(laux)))
# Parte B
print('Entrenadores con mas de 3 toneos ganados')
aux = l1.inicio
while aux is not None:
    if aux.info[1] > 3:
        print(aux.info)
    aux = aux.sig'''
# Parte C
'''aux = l1.inicio
e_mayor = aux.info[1]
while aux is not None:
    if aux.info[1] > e_mayor:
        e_mayor = aux.info[1]
        nom = aux.info
        nod = aux
    aux = aux.sig
print('El entrenador con mayores torneos ganados es: ' + str(nom[0]))
d = nod.lista
dat = d.inicio
p_mayor = dat.info[1]
while dat is not None:
    if dat.info[1] > p_mayor:
        p_mayor = dat.info[1]
        nom1 = dat.info
    dat = dat.sig
print('y su pokemons de mayor nivel es ' + str(nom1))'''
# Parte D

# Parte E
'''dat = l1.inicio
while dat is not None:
    aux1 = dat.lista
    aux = aux1.inicio
    while aux is not None:
        if aux.info[2] == 'fuego' or aux.info[2] == 'planta':
            insertar(l2, dat.info)
        elif aux.info[2] == 'agua' or aux.info[2] == 'volador':
            insertar(l3, dat.info)
        aux = aux.sig
    dat = dat.sig
print('Entrenadores con pokemons de tipo fuego y planta')
barrido(l2)
print('Entrenadores con pokemons de tipo agua y volador')
barrido(l3)'''
# Parte F
'''print('Ingrese el nombre del entrenador')
nombre = input()
aux = l1.inicio
ac = 0
while aux is not None:
    if aux.info[0] == nombre:
        aux1 = aux.lista
        dat = aux1.inicio
        while dat is not None:
            ac = ac + dat.info[1]
            dat = dat.sig
        prom = ac//tamanio(laux)
        print('El nivel de pokemons de ' + nombre + ' es ' + str(prom))
    aux = aux.sig'''
# Parte G
#print('Ingrese el nombre del pokemons')
'''nom = 'Bulbasaur'
aux = l1.inicio
cont = 0
while aux is not None:
    aux1 = aux.lista
    aux2 = aux1.inicio
    while aux2 is not None:
        if aux2.info[0] == nom:
            cont += 1
            insertar(l2, aux.info[0])
        aux2 = aux2.sig
    aux = aux.sig
print('los entrenadores que tienen a ' + nom + ' son:')
barrido(l2)'''
# Parte H


# Ej 15
'''for i in range(1, 8):
    costo = randint(1500, 3500)
    tiempo = randint(2, 12)  # tiempo en horas
    dia = randint(1, 28)
    mes = randint(1, 12)
    anio = randint(2018, 2019)
    persona = 'Persona ' + str(i)
    tarea = [costo, tiempo, dia, mes, anio, persona]
    inserCampo(l1, tarea, 1)
barrido(l1)
aux = l1.inicio'''
# Punto A
'''a = 0
while aux is not None:
    a += aux.info[1]
    aux = aux.sig
prom = (a//7)
print('El tiempo promedio de tareas es de: ' + str(prom) + ' horas')'''

# Punto B
'''a = 0
while aux is not None:
    a += aux.info[0]
    aux = aux.sig
print('El costo total del proyecto es de: $' + str(a))'''
# Punto C
'''while aux is not None:
    if aux.info[5] == 'Persona 5':
        inserCampo(l2, aux.info, 5)
    aux = aux.sig
print('Actividades realizadas por Persona 5: ')
barrido(l2)'''

# Punto D
'''f1 = [7, 8, 2018]
f2 = [5, 9, 2019]
print('Tareas a realizar entre ' + str(f1) + ' y ' + str(f2) + ' : ')
while aux is not None:
    if entre(aux.info[2], f1[0], f2[0]) and entre(aux.info[3], f1[1], f2[1])
    and entre(aux.info[4], f1[2], f2[2]):
        print(aux.info)
    aux = aux.sig'''

# ej16
'''
destinos = ['Paris', 'Atenas', 'Roma', 'Filadelfia', 'Grecia', 'Londres']
for i in range(0, 10):
    empresa = random.choice(string.ascii_uppercase)
    numero = random.randint(0, 50)
    asientos = random.randint(0, 60)
    #fecha =
    origen = random.choice(string.ascii_lowercas)
    destino = random.choice(destinos)
    kilometros = random.randint(10, 1000)
'''
