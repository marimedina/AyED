from hash import crear_tabla_abierta, insert_palabra, barrido_abierta
from hash import busq_palabra, eliminar_palabra, telefono
from hash import crear_tabla_cerrada, rehash, nueva_catedra, barrido_cerrada
from hash import busq_catedra, docente, hash_1, insertar_contacto, insertar_tablaCerrada
from tdalista import *
import random
import string


# Ej 1 - Desarrollar un algoritmo que permita implementar una tabla hash para representar un
# diccionario que permita resolver:
'''
t = crear_tabla_abierta(28)

# Parte A - agregar una palabra y su significado al diccionario
print('Dicc con palabras agregadas:')
insert_palabra(t, 'pesa', 'mancuerna para ejercitar')
insert_palabra(t, 'casa', 'construccion destinada a ser habitada')
insert_palabra(t, 'ventana', 'abertura que brinda iluminacion y ventilacion')
barrido_abierta(t)


# Parte B - determinar si una palabra existe y mostrar su significado
print('')
aux = busq_palabra(t, 'casa')
if aux is not None:
    print('La palabra fue encontrada ' + str(aux.info))
else:
    print('La palabra no se encontro')


# Parte C - borrar una palabra del diccionario
print('')
eliminar_palabra(t, 'casa')
print('Tabla sin palabra casa:')
barrido_abierta(t)
'''


#Ej 2 - Desarrollar un algoritmo que implemente una tabla hash para una guia de telefono, los
# datos que se conocen son numero de telefono, apellido, nombre y direccion de la persona.
# El campo clave debe ser el numero de telufono.
'''
t = crear_tabla_abierta(20)

def hash(telefono):
    area, num = telefono.split("-")
    area = int(area)
    num = int(num)
    return (area + num)


def insert_tel(tabla, telefono, nom_apellido, direccion):
    indice = hash(telefono) % len(tabla)
    campos(tabla[indice], [telefono, nom_apellido, direccion], 0)


for i in range(0, 25):
    insert_tel(t, telefono(), 'Nombre ' + random.choice(string.ascii_uppercase),
              'Direccion ' + random.choice(string.ascii_lowercase))

print('Guia telefonica:')
barrido_abierta(t)

print('')
for i in range(0, len(t)):
    if t[i].tamanio > 0:
        print('En el indice ' + str(i) + ' hay ' + str(t[i]. tamanio) + ' numeros')
'''


#Ej 3 - Implementar un tabla hash cerrada para guardar las catedras de una carrera universitaria
# de acuerdo a su codigo

#a. cargar catedras de una carrera de las cuales se conoce nombre, modalidad cantidad de horas
#b. ademas se deben poder agregar los docentes vinculados con las catedras
#c. debe ser una tabla cerrada
#d. debe poder solucionar las colisiones
'''
t = crear_tabla_cerrada(20)

def cargar_catedra(t, dato):
    clave = hash(dato[0])
    indice = clave % len(t)
    if t[indice] is None:
        t[indice] = dato
    else:
        indice = rehash(t, indice)
        if indice is not None:
            t[indice] = dato
        else:
            print("No hay lugar en la tabla")



for i in range(0, 10):
    catedra = nueva_catedra()
    cargar_catedra(t, catedra)
barrido_cerrada(t)
'''

#Ej 4 - Desarrollar un algoritmo que implemente una tabla hash cerrada para cargar personajes
# de Star Wars de los que solo se conoce su nombre

#a. la tabla inicialmente sera de 20 posiciones
#b. debera permitir el manejo de colisiones
#c. cuando el factor de carga de la tabla exceda el 75%, se debera incrementar el tamanio de la tabla al doble

'''
def carga(t):
    f = 0
    'Para controlar el factor de carga de la tabla'
    ocupados = 0
    for personaje in t:
        if personaje is not None:
            ocupados += 1
    f = (ocupados*100) / len(t)
    return f

def agrandarTabla(t):
    t1 = crear_tabla_cerrada(len(t)*2)
    for personaje in t:
        if personaje is not None:
            insert_perj(t1, personaje)
    return t1

def insert_perj(t, personaje):
    indice = hash_1(personaje)
    indice = indice % len(t)

    if t[indice] is not None:
        indice = rehash(t, indice)
    t[indice] = personaje

    if carga(t) > 75:
        t = agrandarTabla(t)

    return t


t = crear_tabla_cerrada(20)

for i in range(0,15):
    t = insert_perj(t, random.choice(string.ascii_uppercase))

print(len(t)) #Hasta aca tiene 20 posiciones la tabla


t = insert_perj(t, random.choice(string.ascii_uppercase))

print(len(t)) #Se duplico el tamanio
'''



#Ej 5 - Desarrollar un algoritmo que implemente una tabla hash cerrada para administrar los
#contactos de personas de las cuales se conoce nombre, apellido y correo electronico,
#contemplando las siguientes pautas:

#a. El campo clave para generar las posiciones son el apellido y nombre.
#b. Debera contemplar una funcion de sondeo para resolver las colisiones.

'''
t = crear_tabla_cerrada(20)

for i in range(0,10):
    nombre = random.choice(string.ascii_uppercase)
    apellido = random.choice(string.ascii_lowercase)
    correo = random.randint(1, 100)
    contact = [nombre, apellido, correo]
    insertar_contacto(t, contact)

barrido_cerrada(t)
'''


#Ej 6 - Darth Vader le encarga desarrollar los algoritmos para organizar los Troopers cumpliendo
# con ciertas demandas:
'''
legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']
tdigitos = crear_tabla_abierta(2000)
tlegion = crear_tabla_abierta(2000)

# Parte A y B - Generar 2000 Troopers siguiendo el formato contemplando las
# siguientes legiones FL, TF, TK, CT, FN, FO y los digitos generados
#aleatoriamente;

def hashTrooper(clave):
    ind = 0
    if len(clave) == 2:
        ind = (ord(clave[0])*3) + (ord(clave[1])*7)
    else:
        ind = (ord(clave[0])* ord(clave[1])) + ord(clave[2])

    return ind

def busqT(tabla, digitos):
    ind = hashTrooper(digitos)
    ind = ind % len(tabla)

    return tabla[ind]

def nuevoT():
    legion = random.choice(legiones)
    cohoerte = str(random.randint(0,9))
    siglo = str(random.randint(0,9))
    escuadra = str(random.randint(0,9))
    numero = str(random.randint(0,9))
    trooper = legion + '-' + cohoerte + siglo + escuadra + numero

    return trooper

def trooperLegion(tabla, trooper):
    legion, codigo = trooper.split('-')
    indice = hashTrooper(legion)
    indice = indice % len(tabla)
    insertar(tabla[indice], trooper)

def trooperDig(tabla, trooper):
    legion, codigo = trooper.split('-')
    indice = hashTrooper(codigo[1:len(codigo)])
    indice = indice % len(tabla)
    insertar(tabla[indice], trooper)

def agregarT(trooper):
    trooperLegion(tlegion, trooper)
    trooperDig(tdigitos, trooper)




for i in range(0, 20):
    agregarT(nuevoT())

barrido_abierta(tlegion)
barrido_abierta(tdigitos)
print('')
'''
# Parte C - Ahora obtenga todos los Stroormtropers terminados en 781 para asignarlos a una
# mision de asalto y a los terminados en 537 para una mision de exploracion.
'''
asalto = []
buscado = busqT(tdigitos,'781')
if buscado > 0:
    aux = buscado.inicio
    while aux is not None:
        if aux.info[4:] == '781':
            asalto.append(aux.info)
        aux = aux.sig

print('Troopers para mision asalto:')
print(asalto)

exploracion = []
buscado = busqT(tdigitos, '537')
if buscado > 0:
    aux = buscado.inicio
    while aux is not None:
        if aux.info[4:] == '537':
            exploracion.append(aux.info)
        aux = aux.sig
print('Troopers para mision de exploracion:')
print(exploracion)
'''

# Parte D - Ahora obtenga los Strormtroopers de la legion CT para que custodien a Darth
#Vader a una mision de exploracion al planeta Hoth y los de la legion TF para una
#mision de exterminacion a Endor.
'''
exploracion = []
buscado = busqT(tlegion, "CT")
if buscado >= 0:
    print(aca)
    aux = buscado.inicio
    while aux is not None:
        if aux.info[:2] == "CT":
            exploracion.append(aux.info)
        aux = aux.sig
print('Troopers para custodia de Darth Vader:')
print(exploracion)

exterminacion = []
busc = busqT(tlegion, "TF")
if busc >= 0:
    aux = busc.inicio
    while aux is not None:
        if aux.info[0:2] == "TF":
            exploracion.append(aux.info)
        aux = aux.sig
print('Troopers para misison de exterminacion a Endor:')
print(exterminacion)
'''



#Ej 7 - ERROR EN HASH

'''
t_tipo = crear_tabla_cerrada(30)
tipos = ['fuego', 'agua', 'planta', 'normal', 'electrico', 'hielo',
        'lucha', 'veneno', 'tierra', 'volador']

def nuevoP(numero=0):
    num = numero
    nombre = 'Nombre' + str(num)
    c_tipo = random.randint(1,2)
    tipo = random.choice(tipos)
    if c_tipo == 2:
        tipo += '/' + random.choice(tipos)
    nivel = random.randint(0,100)

    return [num, nombre, tipo, nivel]

def hashP(clave):
    if type(clave) is int:
        clave = str(clave)
    indice = 0
    for elemento in clave:
        indice += ord(elemento)
    return indice

def sondeoTipo(tabla, tipo, indice):
    while (tabla[indice] is not None) and (tabla[indice][0] != tipo):
        indice += 1
        if indice == len(tabla):
            indice = 0
    return indice

def insertarNum(tabla, pokemon):
    indice = hashP(pokemon) % len(tabla)
    campos(tabla[indice], pokemon, 0)

def insertarEnTipo(t_tipo, pokemon):
    tip = pokemon[2].split('/')

    for tipo in tip:
        indice = hashP(tipo) % len(t_tipo)
        if t_tipo[indice] is None:
            t_tipo[indice] = [tipo, crear_tabla_abierta(15)]
            insertarNum(t_tipo[indice][1], pokemon)
        else:
            if t_tipo[indice][0] == tipo:
                insertarNum(t_tipo[indice][1], pokemon)
            else:
                indice = sondeoTipo(t_tipos, tipo, indice)
                if t_tipo[indice] is not None:
                    t_tipo[indice] = [tipo, crear_tabla_abierta(15)]
                insertarNum(t_tipo[indice][1], pokemon)

for i in range(15):
    pokemon = nuevoP(i)
    print(pokemon)
    insertarEnTipo(t_tipo, pokemon)
'''

# Ej 8 - la princesa Leia nos encarga el desarrollo de un algoritmo
# de encriptacion para las comunicaciones rebeldes.
'''
def encriptar(texto):
    clave = ''
    for letra in texto:
        p1 = str(ord(letra)*37)
        p2 = hex(ord(letra)*2)
        clave += p1[0] + p2[1] + p2[3] + p1[1] + p1[2] + p2[0] + p1[3] + p2[2]
    return clave


text = 'Ayudame, Obi-Wan Kenobi. Tu eres mi unica esperanza'
texto_encriptado = encriptar(text)
print('Mensaje encriptado:')
print(texto_encriptado)

def desencriptar(clave):
    texto = ''
    while len(clave) > 0:
        caracter = ''
        caracter += clave[0] + clave[3] + clave[4] + clave[6]
        clave = clave[8:]
        caracter = int(caracter)
        caracter = int(caracter/37)
        caracter = chr(caracter)
        texto += caracter
    return texto

print('')
print('Mensaje desencriptado:')
text1 = desencriptar(texto_encriptado)
print(text1)
'''


# Ej 9 - Desarrollar un algoritmo que permita cifrar
# y descifrar un mensaje caracter a caracter
'''
t_valoresCodif = crear_tabla_cerrada(10)
t_valoresCodif[1] = 'abc'
t_valoresCodif[2] = 'def'
t_valoresCodif[3] = 'ghi'
t_valoresCodif[4] = 'jkl'
t_valoresCodif[5] = 'mnn'
t_valoresCodif[6] = 'opq'
t_valoresCodif[7] = 'rst'
t_valoresCodif[8] = 'uvw'
t_valoresCodif[9] = 'xyz'
t_valoresCodif[0] = '#?&'

def hashC(caracter):
    cad = ''
    ascii = ord(caracter)
    ascii = str(ascii)
    for dig in ascii:
        digito = int(dig)
        clave = t_valoresCodif[digito]
        cad += clave
    cad += '%'

    return cad

def encriptar(texto):
    cadena = ''
    for letra in texto:
        cadena += hashC(letra)

    return cadena

texto = 'Ayudame, Obi Wan Kenobi. Tu eres mi unica esperanza'
print('Texto encriptado:')
text_e = encriptar(texto)
print(text_e)

def desencriptar(texto):
    msj = ''
    texto_div = texto.split('%')
    for elemento in texto_div:
        if len(elemento) > 0:
            digitos = ''
            for i in range(0, len(elemento), 3):
                if elemento[i] == "#":
                    digitos += "0"
                elif elemento[i] == "a":
                    digitos += "1"
                elif elemento[i] == "d":
                    digitos += "2"
                elif elemento[i] == "g":
                    digitos += "3"
                elif elemento[i] == "j":
                    digitos += "4"
                elif elemento[i] == "m":
                    digitos += "5"
                elif elemento[i] == "o":
                    digitos += "6"
                elif elemento[i] == "r":
                    digitos += "7"
                elif elemento[i] == "u":
                    digitos += "8"
                elif elemento[i] == "x":
                    digitos += "9"
            digitos = int(digitos)
            msj += chr(digitos)

    return msj
print('')
print('Texto desencriptado:')
text_d = desencriptar(text_e)
print(text_d)
'''

# Ej 10 - Nick Fury director de la agencia S.H.I.E.L.D. intenta detener a la organizacion Hydra y a su
# lider Red Skull, los agentes de la agencia pueden interceptar los mensajes de Hydra pero
# estan cifrados por los cual no pueden hacer nada con estos, por suerte el Capitan America
# en una mision encubierta logro determinar las pautas del metodo de codificacion. Ahora
# Fury nos solicita desarrollar el algoritmo que permita decodificar los mensajes
'''
def calculoComplemento(caracter):
    if ord(caracter) <= 78:
        return 79 + ord(caracter) - 32
    else:
        return 32 + ord(caracter) - 79


def hashS(string):
    hash = 5381
    for caracter in string:
        hash = ((hash << 5) + hash) + ord(caracter)
    return hash & 0xFFFFFFFF

def charAChar(seg):
    n4_dig = ''
    primer_caracter = seg[:4]
    ultimo_caracter = seg[4]
    complemento = ord(ultimo_caracter)
    for elemento in primer_caracter:
        elemento = ord(elemento) - complemento
        elemento = int(sqrt(elemento))
        elemento = str(elemento)
        n4_dig += elemento
    n4_dig = int(n4_dig)
    chr_ascii = int(n4_dig/37)
    caracter = chr(chr_ascii)
    return caracter

def charA5Char(caracter):
    caracteres = ''
    char_ascii = ord(caracter)
    char_ascii *= 37
    complemento = calculoComplemento(caracter)
    char_ascii = str(char_ascii)
    for digito in char_ascii:
        digito = int(digito)
        num = pow(digito, 2) + complemento
        caracter = chr(int(num))
        caracteres += caracter
    caracteres += chr(complemento)

    return caracteres

def decodificar(mensaje):
    texto = ""
    i = 0
    while i < len(mensaje):
        segmento = mensaje[i:i+5]
        indice = hashS(segmento) % len(tabla)
        if (tabla[indice] is None):
            caracter = charAChar(segmento)
            tabla[indice] = caracter
        else:
            caracter = tabla[indice]
        texto += caracter
        i += 5
    return texto

t = crear_tabla_cerrada(227)

#Abro y leo los msj
archivo = open('msj1.txt', encoding='utf-8')
msj_codif = archivo.read()
archivo.close()

archivo2 = open('msj2.txt', encoding='utf-8')
msj2_codif = archivo2.read()
archivo2.close()

archivo3 = open('msj3.txt', encoding='utf-8')
msj3_codif = archivo3.read()
archivo3.close()

#decodifico los 3
msj_decodif = decodificar(msj_codif)
msj2_decodif = decodificar(msj2_codif)
msj3_decodif = decodificar(msj3_codif)

#Muestro
print('Mensaje 1:', msj_codif)
print('')
print('Mensaje 2:', msj2_codif)
print('')
print('Mensaje 3:', msj3_codif)
'''
