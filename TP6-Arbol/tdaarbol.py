import random
from tdaArchivo import *

class NodoArbol():
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.altura = 0
        self.info = info


def altura(raiz):
    if raiz is None:
        return 0
    else:
        return raiz.altura


def peso(raiz):
    if raiz is not None:
        return 1 + peso(raiz.izq) + peso(raiz.der)
    else:
        return 0


def act_altura(raiz):
    if altura(raiz.izq) > altura(raiz.der):
        raiz.altura = altura(raiz.izq) + 1
    else:
        raiz.altura = altura(raiz.der) + 1
    return raiz


def rot_simple(raiz, c):
    if c:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz
    act_altura(raiz)
    act_altura(aux)
    raiz = aux
    return raiz


def rot_doble(raiz, c):
    if c:
        raiz.izq = rot_simple(raiz.izq, False)
        raiz = rot_simple(raiz, True)
    else:
        raiz.der = rot_simple(raiz.der, True)
        raiz = rot_simple(raiz, False)
    return raiz


def balancear(raiz):
    if raiz is not None:
        if (altura(raiz.izq) - altura(raiz.der) == 2):
            if altura(raiz.izq.izq) >= altura(raiz.izq.der):
                raiz = rot_simple(raiz, True)
            else:
                raiz = rot_doble(raiz, True)
        elif (altura(raiz.der) - altura(raiz.izq) == 2):
            if altura(raiz.der.der) >= altura(raiz.der.izq):
                raiz = rot_simple(raiz, False)
            else:
                raiz = rot_doble(raiz, False)
    return raiz


def insertar(raiz, dato):
    if raiz is None:
        raiz = NodoArbol(dato)
        raiz.info = dato
    else:
        if dato < raiz.info:
            raiz.izq = insertar(raiz.izq, dato)
        else:
            raiz.der = insertar(raiz.der, dato)
    act_altura(raiz)
    raiz = balancear(raiz)

    return raiz

def insertarCampo(raiz, dato, campo=0):
    if (raiz is None):
        raiz = NodoArbol(dato)
    else:
        if (dato[campo] < raiz.info[campo]):
            raiz.izq = insertarCampo(raiz.izq, dato, campo)
        else:
            raiz.der = insertarCampo(raiz.der, dato, campo)

    raiz = balancear(raiz)
    act_altura(raiz)

    return raiz


def busqueda(raiz, buscado):
    pos = None
    if raiz is not None:
        if raiz.info == buscado:
            pos = raiz
        else:
            if buscado < raiz.info:
                pos = busqueda(raiz.izq, buscado)
            else:
                pos = busqueda(raiz.der, buscado)
    return pos


def preorden(raiz):
    if raiz is not None:
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)


def postorden(raiz):
    if raiz is not None:
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)


def inordenInvertido(raiz):
    if raiz is not None:
        inordenInvertido(raiz.der)
        print(raiz.info)
        inordenInvertido(raiz.izq)


def imprimir(raiz, espacios=0):
    if raiz is not None:
        espacios += 5
        imprimir(raiz.der, espacios)
        print(' ' * espacios, str(raiz.info))
        imprimir(raiz.izq, espacios)


def reemplazar(raiz):
    aux = None
    if raiz.der is not None:
        raiz.der == reemplazar(raiz.der)
    else:
        aux = raiz
        raiz = raiz.izq
    return(raiz, aux)


def eliminar(raiz, clave):
    x = None
    if raiz is not None:
        if raiz.info > clave:
            raiz.izq, x = eliminar(raiz.izq, clave)
        else:
            if raiz.info < clave:
                raiz.der, x = eliminar(raiz.der, clave)
            else:
                if raiz.izq is None:
                    x = raiz.info
                    raiz = raiz.der
                else:
                    if raiz.der is None:
                        x = raiz.info
                        raiz = raiz.izq
                    else:
                        raiz.izq, aux = reemplazar(raiz.izq)
                        raiz.info = aux.info
    return(raiz, x)


def busqProx(raiz, buscado):
    aux = None
    if raiz is not None:
        if buscado in raiz.info:
            return raiz
        else:
            aux = busqProx(raiz.izq, buscado)
            if aux is None:
                aux = busqProx(raiz.der, buscado)
    return aux


def busqProxCampo(raiz, buscado, campo):
    aux = None
    if raiz is not None:
        if buscado in raiz.info[campo]:
            return raiz
        else:
            aux = busqProxCampo(raiz.izq, buscado, campo)
            if aux is None:
                aux = busqProxCampo(raiz.der, buscado, campo)
    return aux


def nodosPorNivel(raiz, nivel, nivelAct=0):
    #Cantidad de nodos por nivel
    cant = 0
    if raiz is not None:
        if nivel == nivelAct:
            cant += 1
        nivelAct += 1
        cant += nodosPorNivel(raiz.izq, nivel, nivelAct)
        cant += nodosPorNivel(raiz.der, nivel, nivelAct)
        return cant
    else:
        return 0


'''TIRA ERROR EN POW'''
def cantNodosCompletarNivel(nivel):
    # Nodos que deberia haber para que el nivel este completo
    return pow(2, nivel)


def esHoja(raiz):
    if (raiz.izq is None) and (raiz.der is None):
        return True


def mostrarHojas(raiz):
    if raiz is not None:
        mostrarHojas(raiz.izq)
        if esHoja(raiz):
            print(raiz.info)
        mostrarHojas(raiz.der)


def cantHojasArbol(raiz):
    if raiz is not None:
        if (raiz.izq is None) and (raiz.der is None):
            return 1
        else:
            return cantHojasArbol(raiz.izq) + cantHojasArbol(raiz.der)
    else:
        return 0


def cantNodosArbol(raiz):
    if raiz is None:
        return 0
    else:
        return 1 + cantNodosArbol(raiz.izq) + cantNodosArbol(raiz.der)


def nivelLleno(raiz, nivel):
    return nodosPorNivel(raiz, nivel) == cantNodosCompletarNivel(nivel)

def nivelMax(raiz):
    return raiz.altura - 1

def arbolLleno(raiz):
    nivel_mas_profundo = nivelMax(raiz)
    return nivelLleno(raiz, nivel_mas_profundo)



def obtenerPadre(raiz, buscado):
    aux = None
    if raiz is not None:
        if raiz.info == buscado:
            aux = buscado
        elif ((raiz.izq is not None) and (raiz.izq.info == buscado)) or ((raiz.der is not None) and (raiz.der.info == buscado)):
            aux = raiz
        else:
            if buscado < raiz.info:
                aux = obtenerPadre(raiz.izq, buscado)
            else:
                aux = obtenerPadre(raiz.der, buscado)
    return aux


def arbolDeXNiveles(niveles=0):
    raiz = None
    raiz = insertar(raiz, random.randint(0, 100))
    while raiz.altura-1 != niveles:
        raiz = insertar(raiz, random.randint(0, 100))

    return raiz


def recortarArbol(raiz, bosque, nivACortar, nivelac=0):
    if raiz is not None and nivelac <= nivACortar:
        if nivelac == nivACortar:
            bosque.append(raiz)
        recortarArbol(raiz.izq, bosque, nivACortar, nivelac+1)
        recortarArbol(raiz.der, bosque, nivACortar, nivelac+1)

# --------------- ARBOL HUFFMAN ------------------
# ------------------------------------------------

class NodoArbolHuffman():
    def __init__(self, valor, dato, izq=None, der=None):
        self.izq = izq
        self.der = der
        self.info = dato
        self.valor = valor


def arbolHuffman(tabla, comparacion=None):
    lista = []

    for i in tabla:
        nodo = NodoArbolHuffman(i[0], i[1])
        lista.append(nodo)
    while len(lista) > 1:
        nodo1 = lista.pop(0)
        nodo2 = lista.pop(0)

        nueva_frecuencia = nodo1.valor + nodo2.valor
        nodo3 = NodoArbolHuffman(nueva_frecuencia, None, nodo1, nodo2)
        lista.append(nodo3)

    if comparacion:
        lista.sort(key=comparacion)
    else:
        lista.sort(key=lambda x:x.valor)

    return lista[0]


def deHuffmanADiccionario(raiz, diccionario, codif=''):
    if not esHoja(raiz):
        if hijoIzquierdo(raiz) is not None:
            deHuffmanADiccionario(raiz.izq, diccionario, codif+'0')
        if hijoDerecho(raiz) is not None:
            deHuffmanADiccionario(raiz.der, diccionario, codif+'1')
    else:
        diccionario.setdefault(raiz.info, codif)


def comprimir(arbol, mensaje):
    msjCod = ''
    diccCodificado = {}
    deHuffmanADiccionario(arbol, diccCodificado)

    for caracter in mensaje:
        msjCod += diccCodificado.get(caracter)

    return msjCod


def descomprimir(arbol, mensaje):
    msjDescodificado = ''
    raiz = arbol

    while len(mensaje) >= 1:
        while not esHoja(raiz):
            if len(mensaje) > 0:
                caracter = mensaje[0]
                mensaje = mensaje[1:]
            if caracter == '0':
                raiz = raiz.izq
            else:
                raiz = raiz.der
        msjDescodificado += raiz.info
        raiz = arbol

    return msjDescodificado


# --------------- ARBOL DE DEcISION ------------------
# ----------------------------------------------------

class NodoArbolDecision():

    def __init__(self, dato, peso=0, izq=None, der=None):
        self.info = dato
        self.peso = peso
        self.izq = izq
        self.der = der


def insertarArbolDec(raiz, dato, peso):
    if raiz is None:
        raiz = NodoArbolDecision(dato, peso)
    else:
        if peso < raiz.peso:
            raiz.izq = insertarArbolDec(raiz.izq, dato, peso)
        else:
            raiz.der = insertarArbolDec(raiz.der, dato, peso)
    return raiz




# --------------- PARA EJERCICIO 1 ------------------

def nodoRepetido(raiz):
    if raiz is not None:
        if busqueda(raiz.izq, raiz.info) is not None:
            print('Se repite', raiz.info)
        if busqueda(raiz.der, raiz.info) is not None:
            print('Se repite', raiz.info)
        nodoRepetido(raiz.izq)
        nodoRepetido(raiz.der)

def numParImpar(raiz):
    if raiz is not None:
        if raiz.info % 2 == 0:
            return(1 + numParImpar(raiz.izq)[0] + numParImpar(raiz.der)[0], 0 + numParImpar(raiz.izq)[1] + numParImpar(raiz.der)[1])
        else:
            return(0 + numParImpar(raiz.izq)[0] + numParImpar(raiz.der)[0], 1 + numParImpar(raiz.izq)[1] + numParImpar(raiz.der)[1])
    else:
        return 0,0


# --------------- PARA EJERCICIO 4 ------------------

def hijoDerecho(raiz):
    return raiz.der

def hijoIzquierdo(raiz):
    return raiz.izq


# --------------- PARA EJERCICIO 5 ------------------

def Villanos(raiz):
    if raiz is not None:
        Villanos(raiz.izq)
        if not raiz.info[1]:
            print(raiz.info)
        Villanos(raiz.der)
'''
def Heroes(raiz):
    if raiz is not None:
        Heroes(raiz.der)
        if raiz.info[0] is True:
            print(raiz.info)
        Heroes(raiz.izq)
'''

def superheroesConC(raiz):
    if raiz is not None:
        superheroesConC(raiz.izq)
        if (raiz.info[0][0] == 'C') and (raiz.info[1] is True):
            print(raiz.info)
        superheroesConC(raiz.der)

def cantidadSuperheroes(raiz):
    if raiz is not None:
        if raiz.info[1]:
            return (1 + cantidadSuperheroes(raiz.izq) + cantidadSuperheroes(raiz.der))
        else:
            return (0 + cantidadSuperheroes(raiz.izq) + cantidadSuperheroes(raiz.der))
    else:
        return 0

def ArmarBosque(raiz, bosque):
    if raiz is not None:
        ArmarBosque(raiz.izq, bosque)
        ArmarBosque(raiz.der, bosque)
        if raiz.info[1] is False:
            bosque[1] = insertar(bosque[1], raiz.info)
        else:
            bosque[0] = insertar(bosque[0], raiz.info)


# --------------- PARA EJERCICIO 7 ------------------

def nodoMaximo(raiz):
    if raiz.der is not None:
        raiz = nodoMaximo(raiz.der)
    return raiz

def nodoMinimo(raiz):
    if raiz.izq is not None:
        raiz = nodoMinimo(raiz.izq)
    return raiz


# --------------- PARA EJERCICIO 12 ------------------

def arbolDecision(asignacion):
    arbol = None
    for item in asignacion:
        arbol = insertarArbolDec(arbol, item.get("mision"), item.get("peso"))
        # Respuesta si
        arbol = insertarArbolDec(arbol, item.get("asignado"), item.get("peso")-500)

    return arbol

def busqHeroes(raiz, mision):
    aux = None
    if raiz is not None:
        if raiz.info == mision:
            aux = raiz.izq.info
        else:
            aux = busqHeroes(raiz.der, mision)
    return aux

def asignarHeroe(mision, arbolD):
    resultado = busqHeroes(arbolD, mision)
    return resultado


# --------------- PARA EJERCICIO 12 ------------------
def arbolMorse(l_morse):
    raiz = NodoArbolDecision(' ', 1650000)
    for item in l_morse:
        raiz = insertarArbolDec(raiz, item[0], item[1])
    return raiz

def desplazarse(raiz, digito):
    if digito == '.':
        return raiz.izq
    elif digito == '-':
        return raiz.der
    else:
        return None

def decodificarSegmento(arbol, segmento):
    aux = arbol
    seg_decod = ''
    for digito in segmento:
        if digito == ' ':
            seg_decod += aux.info
            aux = arbol
        else:
            aux = desplazarse(aux, digito)

    seg_decod += aux.info
    return seg_decod

def decodificarMsj(arbol, codigo):
    msj_decod = ''
    segmentos = codigo.split('/')

    for segmento in segmentos:
        msj_decod += decodificarSegmento(arbol, segmento)

    return msj_decod


# --------------- PARA EJERCICIO 14 ------------------
class PersonajeSW():
    def __init__ (self, nombre='', altura=0, peso=0):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso
        self.estado = True


def iniciarArchivoPersonajes(ruta):
    arch_sw = abrir(ruta)
    limpiar(arch_sw)
    personajes = ['Chewbacca', 'Darth Vader', 'Yoda', 'Luke Skywalker', 'R2-D2', 'C3PO', 'Obi-Wan Kenobi', 'Boba Fett']
    alturas = [2.14, 2.03, 0.66, 1.75, 1.1, 1.67, 1.82, 1.83]
    pesos = [200, 136, 17, 73, 0.37, 85.2, 80, 78.2]

    for i in range(len(personajes)):
        nuevo_personaje = PersonajeSW(personajes[i], alturas[i], pesos[i])
        guardar(arc_sw, nuevo_personaje)

def extraerDatos(ruta):
    archivo = abrir(ruta)
    array = []
    pos = 0
    while pos < len(archivo):
        data_personaje = [leer(archivo, pos), pos]
        array.append(data_personaje)
        pos += 1
    return array


def generarArbolPersonajesNombre(ruta):
    dato_personajes = extraerDatos(ruta)
    raiz = None
    for item in dato_personajes:
        dato = [item[0].nombre, item[1]]
        raiz = insertarCampo(raiz, dato, 0)
    return raiz


# --------------- PARA EJERCICIO 15 ------------------
def nanoMensaje():
    estado = random.choice(['Despejado', 'Nublado', 'Lluvia'])
    humedad = random.choice(['Baja', 'Alta'])
    cod1 = str(random.choice([1, 2]))
    cod2 = str(random.choice([3, 5]))
    cod3 = str(random.choice([7, 8]))
    msj = estado + '-' + humedad + '-' + cod1 + '-' + cod2 + '-' + cod3
    return msj

def comprimirMed(arbol, mensaje):
    msj_codificado = ''
    dicc_codif = {}
    deHuffmanADiccionario(arbol, dicc_codif)
    segmentos = mensaje.split('-')
    for segmento in segmentos:
        msj_codificado += dicc_codif.get(segmento)

    return msj_codificado

def descomprimirMed(arbol, mensaje):
    segmentos = []
    raiz = arbol
    while len(mensaje) >= 1:
        while not esHoja(raiz):
            car = mensaje[0]
            mensaje = mensaje[1:]
            if car == "0":
                raiz = raiz.izq
            else:
                raiz = raiz.der
        segmentos.append(raiz.info)
        raiz = arbol

    return '-'.join(segmentos)


# --------------- PARA EJERCICIO 16------------------
class Pokemon():
    def __init__(self, nombre="", nro=-1, tipos=[], debilidades=[]):
        self.nombre = nombre
        self.nro = nro
        self.tipos = tipos
        self.debilidades = debilidades

    def __str__(self):
        return 'Nombre: ' + str(self.nombre) + ' - Nro: ' + str(self.nro) +
        ' - Tipo/s:' + str(self.tipos) + ' - Debilidades:' + str(self.debilidades)
