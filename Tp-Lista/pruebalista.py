from tdalista import cargaAuto, insertar, eliminar, barrido
from tdalista import lista_vacia, tamanio, Lista, eliminarNodo
from tdalista import cargaString, insertar1, primo, busquedaLista
from tdalista import campos, finLista, buscarEntre
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


#De este tp no se hacen 11, 12, 13 y 19

# NO ANDAN/FALTAN:
# 8 SE CUELGA
# 15-D VER COMO CALCULAR SI UNA FECHA ESTA ENTRE X FECHAS
# 17 FALTA
# 18 FALTA

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

'''while tamanio(l1) < 10:
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

barrido(l1)'''


# ej 9 - Se tiene una lista de canciones, desarrollar un algoritmo que permita realizar:
'''
artistas = ["Arctic monkeys", "The strokes", "Miles Kane", "Oasis",
            "Radiohead", "The killers", "Coldplay", "Kings of leon",
            "The kooks", "Kasabian", "Josh Homme", "Foo fighters"]
for i in range(0, 50):
    nom = 'Nombre: ' + str(random.randint(0, 50))
    artis = random.choice(artistas)
    dur = random.randint(60, 180)
    reprod = random.randint(200, 1000)
    cancion = [nom, artis, dur, reprod]
    campos(l1, cancion, 3)
barrido(l1)

# Parte A - Obtener la informacion de la cancion mas larga.
aux = l1.inicio
clarga = aux
while aux is not None:
    if (aux.info[2] > clarga.info[2]):
        clarga = aux
    aux = aux.sig
print('')
print('La cancion mas larga es ' + str(clarga.info))

# Parte B - Obtener el TOP 5, TOP 10 y TOP 40 de canciones mas escuchadas.
print('')
print('Top 5:')
aux = l1.inicio
for i in range(0, l1.tamanio - 5): # cambiar 5 para top 10 y 40
    aux = aux.sig
while aux is not None:
    print(aux.info)
    aux = aux.sig


# Parte C - Obtener todas las canciones de la banda Arctic Monkeys.
aux = l1.inicio
while aux is not None:
    if aux.info[1] == 'Arctic monkeys':
        insertar(l2, aux.info)
    aux = aux.sig
print('')
print('Canciones de Arctic Monkeys:')
barrido(l2)
'''


# ej10 - Dada una lista que contiene informacion de los personajes de la saga de Star Wars
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
barrido(l1)
'''
# Parte A - Listar todos los personajes de genero femenino.
'''
print('')
print('Lista de personajes femeninos')
aux = l1.inicio
while aux is not None:
    if aux.info[3] == 'Femenino':
        insertar(l2, aux.info)
    aux = aux.sig
barrido(l2)
'''

# Parte B - Listar todos los personajes de especie Droide
'''
print('')
print('Personajes de especie droide:')
aux = l1.inicio
while aux is not None:
    if aux.info[4] == 'droide':
        if (aux.info[6] == 1 or aux.info[6] == 2 or aux.info[6] == 3 or
        aux.info[6] == 4 or aux.info[6] == 5 or aux.info[6] == 6):
            insertar(l3, aux.info)
    aux = aux.sig
barrido(l3)
'''

# Parte C - Mostrar toda la informacion de Darth Vader
'''
print('')
print('Informacion de Darth Vader')
aux = l1.inicio
while aux is not None:
    if aux.info[0] == 'darth vader':
        insertar(l4, aux.info)
    aux = aux.sig
barrido(l4)
'''

# Parte D - Listar los personajes que aparecen en el episodio VII y en los tres anteriores.
'''
print('')
print('Personajes del episodio 4 al 7')
aux = l1.inicio
while aux is not None:
    if (aux.info[6] == 4 or aux.info[6] == 5 or aux.info[6] == 6 or
       aux.info[6] == 7):
        insertar(l5, aux.info)
    aux = aux.sig
barrido(l5)
'''

# Parte E - Mostrar los personajes con edad mayor a 850 anios y de ellos el mayor.
'''
print('')
print('Personajes mayores a 850 anios')
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
print('')
print('Y de ellos el personaje de mayor edad es:')
print(mayor.info)
'''

# Parte F - Eliminar todos los personajes que solamente aparecieron en los episodios IV, V y VI.
'''
print('')
aux = l1.inicio
print('Sin personajes de episodios 4, 5 y 6')
while aux is not None:
    if aux.info[6] == 4 or aux.info[6] == 5 or aux.info[6] == 6:
        eliminar(l1, aux.info)
    aux = aux.sig
barrido(l1)
'''

# Parte G - Listar los personajes especie humana cuyo planeta de origen es Alderan.
'''
print('')
aux = l1.inicio
while aux is not None:
    if aux.info[4] == 'humano':
        if aux.info[5] == 'alderan':
            insertar(l3, aux.info)
    aux = aux.sig
print('Personajes humanos de Alderan:')
barrido(l3)
'''

# Parte H - Mostrar toda la informacion de los personajes cuya altura es menor a 70
'''
print('')
print('Personajes con menos de 70 centimetros')
aux = l1.inicio
while aux is not None:
    if aux.info[1] < 70:
        print(aux.info)
    aux = aux.sig
'''

# Parte I - Eliminar el anteultimo nodo de una lista
'''
print('')
aux = l1.inicio
while aux.sig.sig is not None:
    aux = aux.sig
eliminar(l1, aux.info)
print('Lista sin el ante ultimo elemento')
barrido(l1)
'''

# Parte J - Determinar en que episodios aparece Chewbacca y mostrar ademas toda su info.
'''
print('')
aux = l1.inicio
while aux is not None:
    if aux.info[0] == 'chewbacca':
        insertar(l4, aux.info[6])
        insertar(l5, aux.info)
    aux = aux.sig
print('Chewbacca aparece en los episodios:')
barrido(l4)
print('Informacion completa:')
barrido(l5)
'''


#ej14 - Se tiene una lista de entrenadores Pokemon.Se conoce de ellos nombre, cantidad de
#torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ademas
#la lista de sus Pokemons de los cuales se conoce: nombre, nivel, tipo y subtipo.
'''
l1 = Lista2()
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
barrido2(l1)
'''

# Parte A - Obtener la cantidad de Pokemons
'''
print('')
print('Cantidad de pokemons por jugador: ' + str(tamanio2(laux)))
'''

# Parte B - Listar los entrenadores que hayan ganado mas de tres torneos.
'''
print('')
print('Entrenadores con mas de 3 toneos ganados:')
aux = l1.inicio
while aux is not None:
    if aux.info[1] > 3:
        print(aux.info)
    aux = aux.sig
'''

# Parte C - Pokemon de mayor nivel del entrenador con mayor cantidad de torneos ganados
'''
print('')
aux = l1.inicio
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
print('y su pokemons de mayor nivel es ' + str(nom1))
'''

# Parte D - Entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 porciento
'''
print('')
cb = 0 #cantidad de batallas totales
porc = 0
aux = l1.inicio
while aux is not None:
    cb += aux.info[2] #perdi 7
    cb += aux.info[3] #gane 3
    porc = (aux.info[3] * 100) / cb
    print(porc)

    if porc > 79:
        insertar(l2, aux.info)
    aux = aux.sig
print('Entrenadores con 79% de batallas ganadas:')
barrido(l2)
'''


# Parte E - Los entrenadores que tengan Pokemons de tipo fuego y planta o agua/volador.
'''
dat = l1.inicio
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
barrido(l3)
'''

# Parte F - promedio de nivel de los Pokemons de un determinado entrenador.
'''
print('')
print('Ingrese el nombre del entrenador')
nombre = 'Alicia' #input()
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
    aux = aux.sig
'''

# Parte G - Determinar cuantos entrenadores tienen a un determinado Pokemon.
'''
print('')
nom = 'Bulbasaur'
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
print('Los entrenadores que tienen a ' + nom + ' son:')
barrido(l2)
'''

# Parte H - Mostrar los entrenadores que tienen Pokemons repetidos.
'''
print('')
aux = l1.inicio
while aux is not None:
    aux1 = aux.lista.inicio
    while aux1.sig is not None:
        #print(aux1.info)
        if (aux1.info[0] == aux1.sig.info[0]):
            print('Un entrenador con pokemon repetido es ' + aux.info[0])
        aux1 = aux1.sig
    aux = aux.sig
'''

# Ej 15
'''
for i in range(1, 8):
    costo = random.randint(1500, 3500)
    tiempo = random.randint(2, 12)  # tiempo en horas
    dia = random.randint(1, 28)
    mes = random.randint(1, 12)
    anio = random.randint(2018, 2019)
    persona = 'Persona ' + str(i)
    tarea = [costo, tiempo, dia, mes, anio, persona]
    insertar(l1, tarea)
barrido(l1)
aux = l1.inicio
'''

# Parte A - Tiempo promedio de tareas
'''
print('')
a = 0
while aux is not None:
    a += aux.info[1]
    aux = aux.sig
prom = (a//7)
print('El tiempo promedio de tareas es de: ' + str(prom) + ' horas')
'''

# Parte B - Costo total del proyecto
'''
print('')
a = 0
while aux is not None:
    a += aux.info[0]
    aux = aux.sig
print('El costo total del proyecto es de: $' + str(a))
'''

# Parte C - Actividades realizadas por una determinada persona
'''
print('')
pers = 'Persona 5'
while aux is not None:
    if aux.info[5] == pers:
        campos(l2, aux.info, 5)
    aux = aux.sig
print('Actividades realizadas por ' + pers + ':')
barrido(l2)
'''

# Parte D
'''
f1 = [1, 8, 2018]
f2 = [21, 9, 2019]
print('Tareas a realizar entre ' + str(f1) + ' y ' + str(f2) + ' : ')
while aux is not None:
    if buscarEntre(aux.info[4], f1[2], f2[2]) and buscarEntre(aux.info[3], f1[1], f2[1])
        and buscarEntre(aux.info[2], f1[0], f2[0]):
        print(aux.info)
    aux = aux.sig
'''



# ej16 - Se tiene los vuelos de un aeropuerto de los cuales se conoce empresa, numero, cantidad
# de asientos, fecha, origen, destino, km del vuelo, y de cada vuelo ademas se tiene la
# informacion de cada asiento: numero, clases, estado, persona.
'''
l2 = Lista2()
destinos = ['Paris', 'Atenas', 'Roma', 'Filadelfia', 'Grecia', 'Londres']
estado_asientos = ['libre', 'ocupado']
empresas = ['Arg', 'Bra', 'Col', 'Uru', 'Par', 'Can']
clases_as = ['turista', 'primera clase']
for i in range(0, 6):
    empresa = empresas[i]
    numero = random.randrange(1, 6)
    asientos = random.randint(0, 60)
    dia = random.randint(1,30)
    mes = random.randint(1,12)
    origen = random.choice(string.ascii_uppercase)
    destino = destinos[i]
    km = random.randint(10, 1000)
    vuelos = [empresa, numero, asientos, dia, mes, origen, destino, km]
    campos2(l2, vuelos, 0)
    nodo = busquedacampos2(l2, vuelos[0], 0)
    laux = nodo.lista
    for j in range(0,3):
        num = random.randint(0,90)
        clase = random.choice(clases_as)
        estado = random.choice(estado_asientos)
        persona = random.choice(string.ascii_uppercase)
        asiento = [num, clase, estado, persona]
        campos2(laux, asiento, 0)
barrido2(l2)
'''

#Parte A - Lista los vuelos con destino a Atenas
'''
print('')
print('Vuelos con destino a Atenas:')
aux = l2.inicio
while aux is not None:
    if aux.info[6] == 'Atenas':
        insertar(l1, aux.info)
    aux = aux.sig
barrido(l1)
'''

#Parte B - Listar los vuelos con asientos clase turista disponible.
'''
print('')
print('Vuelos con asientos de clase turista:')
aux = l2.inicio
while aux is not None:
    aux1 = aux.lista.inicio
    while aux1 is not None:
        if aux1.info[1] == 'turista' and aux1.info[2] == 'libre':
            insertar(l1, aux.info)
        aux1 = aux1.sig
    aux = aux.sig
barrido(l1)
'''

#Parte C - Mostrar el total recaudado por cada vuelo, considerando clase turista $350 por
#km y primera clase $988 por km
'''
print('')
print('Total recaudado por cada vuelo:')
tr = 0 #total recaudado
aux = l2.inicio
while aux is not None:
    aux1 = aux.lista.inicio
    while aux1 is not None:
        tk = aux.info[7]
        if aux1.info[1] == 'turista':
            ac = tk * 350
        else:
            ac = tk * 988
        print(aux.info)
        print('Su total recaudado es: ' + str(ac))
        aux1 = aux1.sig
    aux = aux.sig
'''


#Parte D - Los vuelos programados para una determinada fecha
'''
print('')
print('Vuelos con fecha 12/02/2020:')
aux = l2.inicio
while aux is not None:
    if aux.info[3] == 12 and aux.info[4] == 2:
        insertar(l1, aux.info)
    aux = aux.sig
barrido(l1)
'''

#Parte E - Vender un asiento (pasaje) para un determinado vuelo.
'''
print('')
print('Vender un pasaje')
aux = l2.inicio
while aux is not None:
    if aux.info[6] == 'Filadelfia':
        aux1 = aux.lista.inicio
        while aux1 is not None:
            if aux1.info[2] == 'libre':
                aux1.info[2] = 'ocupado'
            aux1 = aux1.sig
    aux = aux.sig
barrido2(l2)
'''

#Parte F - Eliminar un vuelo. Tener en cuenta que si tiene pasajes vendidos, se deben
#conocer los datos de dicha persona
'''
print('')
print('Eliminar vuelo con destino a Roma')
aux = l2.inicio
while aux is not None:
    if aux.info[6] == 'Roma':
        aux1 = aux.lista.inicio
        while aux1 is not None:
            if aux1.info[2] == 'ocupado':
                print('Datos de la persona a la que se le vendio el asiento:')
                print(aux1.info[3])
            aux1 = aux1.sig
        eliminar(l2, aux.info)
    aux = aux.sig
print('')
barrido2(l2)
'''


#ej20

for i in range(1, 8):
    producto = 'Producto ' + random.choice(string.ascii_uppercase)
    costo = '$' + str(random.randint(1500, 3500))
    calif = random.randint(1, 5)
    productos = [producto, costo, calif]
    insertar(l1, productos)
barrido(l1)

# Parte A - Mostrar los datos de un determinado producto.
'''
print('')
print('Mostrando datos del producto A')
aux = l1.inicio
while aux is not None:
    if aux.info[0] == 'Producto A':
        print(aux.info)
    aux = aux.sig
'''


#Parte B
#Por defecto los productos ya estan ordenados por nombre.

#Parte C
print('')
aux = l1.inicio
while aux is not None:
    insertar1(l2, aux.info, 2)
    aux = aux.sig
print('Listado de productos ordenado por calificacion')
barrido(l2)


#Parte D - Mostrar el producto mas barato de calificacion 3.
'''
print('')
menor = 0
producto = None
aux = busquedacampos2(l1, 3, 2)
if aux is not None:
    menor = aux.info[1]
    producto = aux.info[0]
while (aux is not None) and (aux.info[2] == 3):
    if menor >= aux.info[1]:
        menor = aux.info[1]
        producto = aux.info[0]
    aux = aux.sig
print('El producto mas barato de calificacion 3 es el ' + str(producto) + ' y su precio es ' + str(menor))
'''

#Parte E
'''
print('')
aux = l1.inicio
while aux is not None:
    if aux.info[0] == 'Producto H':
        insertar(l2, aux.info[1])
    aux = aux.sig
print('El precio de los productos H es:')
barrido(l2)
'''
