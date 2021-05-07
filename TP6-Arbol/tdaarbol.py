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

def eliminarCampo(raiz, clave, campo):
    x = None
    if (raiz is not None):
        if (raiz.info[campo] > clave):
            raiz.izq, x = eliminarCampo(raiz.izq, clave, campo)
        else:
            if(raiz.info[campo] < clave):
                raiz.der, x = eliminarCampo(raiz.der, clave, campo)
            else:  # Si es igual
                if (raiz.izq is None):
                    x = raiz.info
                    raiz = raiz.der
                else:
                    if(raiz.der is None):
                        x = raiz.info
                        raiz = raiz.izq
                    else:
                        raiz.izq, aux = reemplazar(raiz.izq)
                        raiz.info = aux.info
    return (raiz, x)

def busquedaCampo(raiz, buscado, campo=0):
    aux = None
    if (raiz is not None):
        if (raiz.info[campo] == buscado):
            aux = raiz
        else:
            if (buscado < raiz.info[campo]):
                aux = busquedaCampo(raiz.izq, buscado, campo)
            else:
                aux = busquedaCampo(raiz.der, buscado, campo)
    return aux

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

def busquedaKnuth(raiz, buscado):
    aux = None
    if raiz is not None:
        if raiz.info == buscado:
            return raiz
        else:
            aux = busquedaKnuth(raiz.izq, buscado)
            if not aux:
                aux = busquedaKnuth(raiz.der, buscado)
    return aux


def busquedaCoincidenciasKnuth(raiz, buscado, lista_coincidencias=[]):
    if raiz is not None:
        if buscado in raiz.info:
            lista_coincidencias.append(raiz)
        busquedaCoincidenciasKnuth(raiz.izq, buscado, lista_coincidencias)
        busquedaCoincidenciasKnuth(raiz.der, buscado, lista_coincidencias)


def busquedaCoincidenciasKnuthCampo(raiz, buscado, campo,lista_coincidencias=[]):
    if raiz is not None:
        if buscado in raiz.info[campo]:
            lista_coincidencias.append(raiz)
        busquedaCoincidenciasKnuthCampo(raiz.izq, buscado, campo, lista_coincidencias)
        busquedaCoincidenciasKnuthCampo(raiz.der, buscado, campo, lista_coincidencias)


def busquedaCampoKnuth(raiz, buscado, campo=0):
    aux = None
    if raiz is not None:
        if raiz.info[campo] == buscado:
            return raiz
        else:
            aux = busquedaCampoKnuth(raiz.izq, buscado, campo)
            if not aux:
                aux = busquedaCampoKnuth(raiz.der, buscado, campo)
    return aux


def getHijosEnlazados(nodo_nario):
    inicio, aux = None, None

    if len(nodo_nario.hijos) > 0:
        info_hijo = nodo_nario.hijos.pop(0).info
        nodo_b = NodoArbol(info_hijo)

        inicio = nodo_b
        aux = inicio

    for hijo_restante in nodo_nario.hijos:
        info = hijo_restante.info
        nodo_b = NodoArbol(info)

        aux.der = nodo_b
        aux = nodo_b
    return inicio


def transformarKnuth(raiz_nario):
    arbol_k = NodoArbol(raiz_nario.info)
    cola = Cola()
    narioToCola(raiz_nario, cola)
    nodos_n = colaToList(cola)

    for nodo in nodos_n:
        hijos_puntero_inicio = getHijosEnlazados(nodo)

        if hijos:
            respuesta = busquedaKnuth(arbol_k, nodo.info)

            if respuesta:
                respuesta.izq = hijos_puntero_inicio

    return arbol_k


def barridoKnuth(arbol):
    if arbol is not None:
        print(arbol.info)
        barridoKnuth(arbol.izq)
        barridoKnuth(arbol.der)

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


# --------------- ARBOL N-ARIO ------------------
# ----------------------------------------------------

class NodoNario(object):

    def __init__(self, info):
        self.info = info
        self.hijos = []


def esTitulo1(linea):
    return linea[:10].count(".") == 1


def esTitulo2(linea):
    return linea[:10].count(".") == 2


def esTitulo3(linea):
    return linea[:10].count(".") == 3


def insertarNario(raiz, info_padre, info):
    if raiz is None:
        raiz = NodoNario(info)
    else:
        nodo_padre = busquedaNario(raiz, info_padre)

        if nodo_padre:
            hijo = NodoNario(info)
            nodo_padre.hijos.append(hijo)

    return raiz


def busquedaNario(raiz, buscado, aux=None):

    if (raiz is not None) and (aux is None):
        if (raiz.info == buscado):
            aux = raiz
        else:
            for hijo in raiz.hijos:
                aux = busquedaNario(hijo, buscado, aux)
    return aux


def barridoNario(raiz):
    if raiz is not None:
        print(raiz.info)
        for hijo in raiz.hijos:
            barridoNario(hijo)


def fileToNario(archivo):
    arbol = None
    pos = 0

    arbol = insertarNario(arbol, None, "INDICE")
    largo_archivo = len(archivo)

    ultimo_titulo1 = None
    ultimo_titulo2 = None


    while pos < largo_archivo:
        line = leer(archivo, pos)
        line = line.replace("\n", "")

        if esTitulo1(line):
            arbol = insertarNario(arbol, arbol.info, line)

            ultimo_titulo1 = line

        if esTitulo2(line):
            padre = ultimo_titulo1
            arbol = insertarNario(arbol, padre, line)

            ultimo_titulo2 = line

        if esTitulo3(line):
            padre = ultimo_titulo2
            arbol = insertarNario(arbol, padre, line)

        pos += 1
        line = leer(archivo, pos)

    return arbol


def narioToCola(arbol_n, cola):
    if arbol_n is not None:
        arribo(cola, arbol_n)

        for hijo in arbol_n.hijos:
            narioToCola(hijo, cola)

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

# --------------- PARA EJERCICIO 3 ------------------

def recDer(nodo):
    aux = nodo
    while aux:
        print(aux.info)
        aux = aux.der


def mostrarParte(arbol, buscado):
    respuesta = busquedaKnuth(arbol, buscado)
    if respuesta:
        print(respuesta.info)
        barridoKnuth(respuesta.izq)

def getPagina(arbol, buscado):
    respuesta = busquedaKnuth(arbol, buscado)
    if respuesta:
        info = respuesta.info
        fragmentos = info.split(" ")
        pagina = fragmentos[-1]
        if pagina.isnumeric():
            return pagina
        else:
            return -1
    else:
        return -1

def contarCantidadCapitulos(inicio_indice):
    cantidad = 0

    aux = inicio_indice.izq
    while aux is not None:
        cantidad += 1
        aux = aux.der
    return cantidad


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
class PersonajeStarWars():
    def __init__ (self, nombre='', altura=0, peso=0):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso
        self.estado = True


def initArchivoPersonajes(ruta):
    arch_sw = abrir(ruta)
    limpiar(arch_sw)
    personajes = ['Chewbacca', 'Darth Vader', 'Yoda', 'Luke Skywalker', 'R2-D2', 'C3PO', 'Obi-Wan Kenobi', 'Boba Fett']
    alturas = [2.14, 2.03, 0.66, 1.75, 1.1, 1.67, 1.82, 1.83]
    pesos = [200, 136, 17, 73, 0.37, 85.2, 80, 78.2]

    for i in range(len(personajes)):
        nuevo_personaje = PersonajeStarWars(personajes[i], alturas[i], pesos[i])
        guardar(arc_sw, nuevo_personaje)

def extraerDataPersonajes(ruta):
    archivo = abrir(ruta)
    array = []
    pos = 0
    while pos < len(archivo):
        data_personaje = [leer(archivo, pos), pos]
        array.append(data_personaje)
        pos += 1
    return array


def generarArbolPersonajesNombre(ruta):
    dato_personajes = extraerDataPersonajes(ruta)
    raiz = None
    for item in dato_personajes:
        dato = [item[0].nombre, item[1]]
        raiz = insertarCampo(raiz, dato, 0)
    return raiz


def obtenerIndice(arbol, buscado):
    resultado = busquedaCampo(arbol, buscado, 0)
    if resultado:
        return resultado.info[1]
    else:
        return -1


def altaPersonaje(arbol, ruta_archivo):
    nombre = input('Ingrese el nombre del personaje: ')
    altura = float(input('Ingrese la altura del personaje: '))
    peso = float(input('Ingrese el peso del personaje: '))

    personaje = PersonajeStarWars(nombre, altura, peso)

    archivo = abrir(ruta_archivo)
    guardar(archivo, personaje)
    cerrar(archivo)

    arbol = generarArbolPersonajesNombre(ruta_archivo)

    return arbol


def modificarPersonaje(arbol, ruta_archivo):
    archivo = abrir(ruta_archivo)

    buscado = input("Nombre del personaje buscado: ")

    indice = obtenerIndice(arbol, buscado)

    if indice == -1:
        print("Personaje no encontrado")
    else:
        personaje = leer(archivo, indice)

        print("1- Nombre:", personaje.nombre)
        print("2- Altura:", personaje.altura)
        print("3- Peso:", personaje.peso)
        opcion = input("Seleccione campo a modificar: ")
        print()

        if (opcion in ["1", "2", "3"]):
            nuevo_valor = input("Nuevo valor: ")

            if opcion == "1":
                personaje.nombre = nuevo_valor
            elif opcion == "2":
                personaje.altura = float(nuevo_valor)
            elif opcion == "3":
                personaje.peso = float(nuevo_valor)

            modificar(archivo, personaje, indice)
            cerrar(archivo)

            arbol = generarArbolPersonajesNombre(ruta_archivo)
            print("Personaje Guardado")
        else:
            print("Opcion seleccionada incorrecta")

    return arbol


def bajaPersonaje(arbol, ruta_archivo):
    archivo = abrir(ruta_archivo)

    buscado = input("Nombre del personaje buscado: ")

    indice = obtenerIndice(arbol, buscado)

    if indice == -1:
        print("Personaje no encontrado")
    else:
        personaje = leer(archivo, indice)
        personaje.estado = False

        modificar(archivo, personaje, indice)
        cerrar(archivo)

        print("Personaje dado de baja")

        arbol = generarArbolPersonajesNombre(ruta_archivo)

    return arbol


def consultaPersonaje(arbol, buscado, ruta_archivo):
    archivo = abrir(ruta_archivo)

    indice = obtenerIndice(arbol, buscado)

    if indice == -1:
        print("El personaje buscado no se encuentra")
    else:
        personaje = leer(archivo, indice)
        print("Nombre:", personaje.nombre)
        print("Altura:", personaje.altura)
        print("Peso:", personaje.peso)
        print()


def listadoIndicesAltura(arbol, archivo):
    if arbol is not None:
        listadoIndicesAltura(arbol.izq, archivo)

        indice = obtenerIndice(arbol, arbol.info[0])
        if indice != -1:
            personaje = leer(archivo, indice)
            if (personaje.estado) and (personaje.altura > 1):
                print("Nombre:", personaje.nombre)
                print("Altura:", personaje.altura)
                print("Peso:", personaje.peso)
                print()

        listadoIndicesAltura(arbol.der, archivo)


def listadoIndicesPeso(arbol, archivo):
    if arbol is not None:
        listadoIndicesPeso(arbol.izq, archivo)

        indice = obtenerIndice(arbol, arbol.info[0])
        if indice != -1:
            personaje = leer(archivo, indice)
            if (personaje.estado) and (personaje.peso < 75):
                print("Nombre:", personaje.nombre)
                print("Altura:", personaje.altura)
                print("Peso:", personaje.peso)
                print()

        listadoIndicesPeso(arbol.der, archivo)

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


# --------------- PARA EJERCICIO 17------------------
def generarRegistro(codigo=0):
    grs = ['Kylo Ren', 'Hux', 'Capitana Phasma']
    soldados = ['Imperial Stromtrooper', 'Imperial Scout Trooper', 'Imperial Death Trooper',
    'Sith Trooper', 'First Order Stromtrooper']
    fechas = ['01/01/2001', '02/02/2002', '03/03/2003', '04/04/2004', '05/05/2005', '06/06/2006',
    '07/07/2007', '08/08/2008', '09/09/2009', '10/10/2010', '11/11/2011', '12/12/2012']
    general = random.choice(grs)
    fecha_mision = random.choice(fechas)
    '''True = no fallo, False = si fallo'''
    estado = random.choice([True, False])
    soldado = random.choice(soldados)

    reg_mision = [general, fecha_mision, codigo, estado, soldado]

    return reg_mision

def obtenerNombre(arbol, nombre, lista):
    if (arbol is not None) and (arbol.info[0] == nombre):
        lista.append(arbol.info)
        obtenerNombre(arbol.izq, nombre, lista)
        obtenerNombre(arbol.der, nombre, lista)

def listarXNombre(arbol, nombre):
    aux = busquedaCampo(arbol, nombre, 0)
    list = []
    if aux:
        obtenerNombre(aux, nombre, list)

    return list

def armasFalladas(arbol):
    '''True si no fallaron, false si fallaron'''
    grs = ['Kylo Ren', 'Hux', 'Capitana Phasma']
    for gr in grs:
        regs = listarXNombre(arbol, gr)
        fallas = 0
        for reg in regs:
            if not reg[3]:
                fallas += 1
        print('La cantidad de armas del general ', gr, 'que fallaron fueron ', fallas)


def cantSoldados(arbol, general):
    tipos = ['Imperial Stromtrooper', 'Imperial Scout Trooper', 'Imprerial Death Trooper',
        'Sith Trooper', 'First Order Stromtrooper']
    reportes = listarXNombre(arbol, general)
    cantidad = {}
    for soldado in tipos:
        cantidad.setdefault(str(soldado), 0)
    for reporte in reportes:
        soldado = reporte[4]
        cantidad[soldado] += 1
    print(cantidad)


def cantSoldados(arbol, soldado, cant_soldado=0, cant_fallas=0):
    if arbol is not None:
        cant_soldado, cant_fallas = cantSoldados(arbol.izq, soldado, cant_soldado, cant_fallas)
        if arbol.info[4] == soldado:
            if arbol.info[3]:
                cant_fallas += 1
            cant_soldado += 1
        cant_soldado, cant_fallas = cantSoldados(arbol.der, soldado, cant_soldado, cant_fallas)
    return cant_soldado, cant_fallas


def Sith_Fallas(arbol):
    cant_sith, cant_fallas = cantSoldados(arbol, 'Sith Trooper')
    print('La cantidad de Sith en las misiones son ', cant_sith, ' y a ', cant_fallas, ' le fallaron los blasters')


def obtenerFecha(arbol, fecha, lista):
    if (arbol is not None) and (arbol.info[1] == fecha):
        lista.append(arbol.info)
        obtenerFecha(arbol.izq, fecha, lista)
        obtenerFecha(arbol.der, fecha, lista)


def listadoPorFecha(arbol, fecha):
    puntero_resultado = busquedaCampo(arbol, fecha, 1)
    lista = []
    if puntero_resultado:
        obtenerFecha(puntero_resultado, fecha, lista)
    return lista


def codMision(arbol, fecha_buscada):
    l_reportes = listadoPorFecha(arbol, fecha_buscada)

    for reporte in l_reportes:
        print('Codigo de blasters de mision: ', reporte[2])



# --------------- PARA EJERCICIO 18------------------
class Libro():
    def __init__(self, titulo, isbn, autores, editorial, cant_pag):
        self.titulo = titulo
        self.isbn = isbn
        self.autores = autores
        self.editorial = editorial
        self.cant_pag = cant_pag

    def __str__(self):
        return ('Titulo: ' + str(self.titulo) + ' - ISBN: ' + str(self.isbn) + ' - Autores: '
                + str(self.autores) + ' - Editorial: ' + str(self.editorial) + ' - Paginas: ' + str(self.cant_pag))

def definirAutores(autores):
    lista_autores = []

    cant = randint(1, 3)
    while (len(lista_autores) < cant):
        nuevo_autor = choice(autores)
        if nuevo_autor not in lista_autores:
            lista_autores.append(nuevo_autor)

    return lista_autores

def initFileLibros():
    ruta_file = 'Libros/libros'
    titulos = ['Algoritmos', 'Algol', 'Mineria de Datos', 'Base de Datos', 'Sistemas y organizaciones', 'Calculo', 'Redes']
    autores = ['autor1', 'autor2', 'autor3', 'autor4', 'autor5', 'autor6', 'autor7', 'Tanenbaum', 'Connolly', 'Rowling', 'Riordan']
    editoriales = ['edit1', 'edit2', 'edit3', 'edit4', 'edit5']

    archivo = abrir(ruta_file)
    limpiar(archivo)

    for i in range(100):
        titulo = choice(titulos)
        isbn = i
        autor = definirAutores(autores)

        editorial = choice(editoriales)
        cant_pag = randint(100, 2000)

        libro = Libro(titulo, isbn, autor, editorial, cant_pag)
        guardar(archivo, libro)

    cerrar(archivo)

def generarArbolLibro(ruta_file, tipo_gen):
    raiz = None
    dataLibros = fileToArray(ruta_file)
    for item in dataLibros:
        libro = item[0]
        indice = item[1]
        if tipo_gen == 'titulo':
            dato = libro.titulo
        elif tipo_gen == 'isbn':
            dato = libro.isbn
        elif tipo_gen == 'autores':
            dato = libro.autores
        elif tipo_gen == 'paginas':
            dato = libro.cant_pag
        nuevo_libro = [dato, indice]
        raiz = insertarCampo(raiz, nuevo_libro, 0)
    return raiz


def busquedaPorISBN(arbol, buscado):
    resultado = busquedaCampo(arbol, buscado, 0)
    if resultado:
        return resultado.info
    else:
        return None


def proximidadAutor(arbol, buscado, lista=[]):
    if arbol is not None:
        if buscado in arbol.info[0]:
            lista.append(arbol.info)
        proximidadAutor(arbol.izq, buscado, lista)
        proximidadAutor(arbol.der, buscado, lista)


def busquedaPorAutor(arbol, buscado):
    lista_con_autor = []
    proximidadAutor(arbol, buscado, lista_con_autor)
    return lista_con_autor


def proximidadTitulo(arbol, buscado, lista=[]):
    if arbol is not None:
        if(arbol.info[0][0:len(buscado)].lower() == buscado.lower()):
            lista.append(arbol.info)
        proximidadTitulo(arbol.izq, buscado, lista)
        proximidadTitulo(arbol.der, buscado, lista)
    return lista


def busquedaPorCoincidenciaTitulo(arbol, buscado):
    lista_coincidenca_inicio = []
    proximidadTitulo(arbol, buscado, lista_coincidenca_inicio)

    return lista_coincidenca_inicio


def busqPag(arbol, cantidad, lista=[]):
    if (arbol is not None):
        libro = arbol.info
        if libro[0] > cantidad:
            lista.append(libro[1])
        busqPag(arbol.izq, cantidad, lista)
        busqPag(arbol.der, cantidad, lista)


# --------------- PARA EJERCICIO 19 ------------------
class RegistroMeteorologico():

    def __init__(self, temp, presion, humedad, visibilidad, viento):
        self.temp = temp
        self.presion = presion
        self.humedad = humedad
        self.visibilidad = visibilidad
        self.viento = viento

    def __str__(self):
        return "Temp: {} - Presion: {} - Humedad: {} - Visib: {} - Viento: {}".format(self.temp, self.presion, self.humedad, self.visibilidad, self.viento)


def genRegistroMeteorologico():
    temp = round(random.uniform(2,40), 2)
    presion = round(random.uniform(900, 1100), 2)
    humedad = random.randint(50, 99)
    visibilidad = round(random.uniform(5, 20), 2)
    viento = round(random.uniform(1, 15), 2)
    return RegistroMeteorologico(temp, presion, humedad, visibilidad, viento)

def genArbolMeteorologico():
    arbol = None
    datos = [['Visibilidad', 15], ['Humedad', 70], 'Despejado', ['Viento', 8.7], ['Visibilidad', 8], ['Viento', 5], 'Parcialmente Nublado', ['Presion', 1013], ['Humedad', 92], 'Despejado', 'Nublado',
    ['Humedad', 96], ['Viento', 7.2], ['Visibilidad', 12], ['Viento', 12.2], 'Nublado', 'Mayormente Nublado', ['Presion', 1018], 'Nublado', 'Despejado', 'Mayormente Nublado', 'Lluvia', 'Nublado', ['Visibilidad', 1], 'Nublado', 'Lluvia', 'Mayormente Nublado']
    codigo = [3000, 2000, 3010, 1000, 2800, 800, 1500, 2500, 2960, 700, 900, 2400, 2700, 2950, 2990, 2300, 2450, 2600, 2750, 2925, 2955, 2980, 2995, 2550, 2650, 2525, 2578]
    for i in range(len(datos)):
        arbol = insertarCampo(arbol, [datos[i], codigo[i]], 1)

    return arbol

def asignarValorRegistro(registro, key):
    valor = 0
    if key == 'Temperatura':
        valor = registro.temp
    elif key == 'Presion':
        valor = registro.presion
    elif key == 'Humedad':
        valor = registro.humedad
    elif key == 'Visibilidad':
        valor = registro.visibilidad
    elif key == 'Viento':
        valor = registro.viento
    return valor

def definirPronostico(arbol, registro):
    while arbol is not None:
        if esHoja(arbol):
            return arbol.info[0]
        else:
            key = arbol.info[0][0]
            umbral = arbol.info[0][1]

            valor = asignarValorRegistro(registro, key)
            if valor <= umbral:
                arbol = arbol.izq
            else:
                arbol = arbol.der
    return arbol[0]


# --------------- PARA EJERCICIO 21 ------------------

def agregarDescripcion(arbol, criatura, descripcion):
    res = busquedaCampo(arbol, criatura, 0)
    if res:
        res.info[2] = descripcion
    else:
        print('Error, critura no encontrada')

def arbolToArrayCriaturas(arbol, lista=[]):
    if arbol is not None:
        if arbol.info[1] != '':
            lista.append(arbol.info)
        arbolToArrayCriaturas(arbol.izq, lista)
        arbolToArrayCriaturas(arbol.der, lista)

def eliminarDuplicados(lista):
    lista_aux = []
    for item in lista:
        if item not in lista_aux:
            lista_aux.append(item)
    return lista_aux

def vencedores(arbol):
    criaturas_derrotadas = []
    arbolToArrayCriaturas(arbol, criaturas_derrotadas)

    vencedores = []
    for criatura in criaturas_derrotadas:
        vencedores.append(criatura[1])

    return vencedores

def criaturasDerrotadasPor(arbol, heroe, lista=[]):
    if arbol is not None:
        if arbol.info[1] == heroe:
            lista.append(arbol.info)
        criaturasDerrotadasPor(arbol.izq, heroe, lista)
        criaturasDerrotadasPor(arbol.der, heroe, lista)


def busquedaProximidadCriatura(raiz, buscado, lista=[]):
    if (raiz is not None):
        if (buscado.lower() in raiz.info[0].lower()):
            lista.append(raiz.info)
        busquedaProximidadCriatura(raiz.izq, buscado, lista)
        busquedaProximidadCriatura(raiz.der, buscado, lista)


def modificarDerrotadoPor(arbol, criatura, nombre):
    res = busquedaCampo(arbol, criatura, 0)
    if res:
        res.info[1] = nombre
    else:
        print('Error, criatura no encontrada')

def modificarnombreCriatura(arbol, nombre_old, nombre_new):
    res = busquedaCampo(arbol, nombre_old, 0)
    if res:
        res.info[0] = nombre_new
    else:
        print('Error, criatura no encontrada')


# --------------- PARA EJERCICIO 22 ------------------

def formatearTablaParaHuffman(tabla):
    tabla_para_huffman = []

    for elemento in tabla:
        nuevo = [elemento[2], elemento[0]]
        tabla_para_huffman.append(nuevo)

    tabla_para_huffman.sort(key=lambda x: x[0])
    return tabla_para_huffman

def obtenerLargoTotal(tabla):
    total = 0
    for item in tabla:
        total += item[1]
    return total

def asignarFrecuencias(tabla):
    largo_total = obtenerLargoTotal(tabla)

    for item in tabla:
        item[2] = item[1] / largo_total

def descomprimir2(arbol, cadena):
    msj_decodificado = ''
    raiz_aux = arbol
    pos = 0
    while(pos < len(cadena)):
        if(cadena[pos] == '0'):
            raiz_aux = raiz_aux.izq
        else:
            raiz_aux = raiz_aux.der
        pos += 1
        if(raiz_aux.izq is None):
            msj_decodificado += raiz_aux.info
            raiz_aux = arbol
    return msj_decodificado
