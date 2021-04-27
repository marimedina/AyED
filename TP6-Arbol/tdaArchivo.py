import shelve
from os import remove


def abrir(ruta):
    return shelve.open(ruta)


def cerrar(archivo):
    archivo.close()


def leer(archivo, pos):
    try:
        return archivo[str(pos)]
    except Exception:
        return None

def leerIndices(archivo, indices=[]):
    '''Devuelve una lista de los elementos del archivo que pudo leer en las posiciones dadas'''
    resultados = []
    for indice in indices:
        resultados.append(leer(archivo, indice))
    return resultados

def guardar(archivo, dato):
    try:
        archivo[str(len(archivo))] = dato
    except Exception:
        raise Exception


def modificar(archivo, dato, pos):
    try:
        archivo[str(pos)] = dato
        return True
    except Exception:
        raise Exception


def barridoArchivo(archivo):
    '''Imprime el dato de cada posicion'''
    pos = 0
    while pos < len(archivo):
        print(leer(archivo, pos))
        pos += 1


def fileToArray(ruta):
    '''Devuelve array con los datos y la posicion de cada pokemon almacenado en el archivo'''
    archivo = abrir(ruta)
    array = []
    pos = 0
    while pos < len(archivo):
        data_elemento = [leer(archivo, pos), pos]
        array.append(data_elemento)
        pos += 1
    cerrar(archivo)
    return array


def txtToDat(rutatxt="", rutadat=""):
    '''Crea o sobreescribe archivo.dat a partir de .txt'''
    # Abrir archivo dir
    archivodat = abrir(rutadat)
    #Si ya existe, limpiamos el .dat
    limpiar(archivodat)
    # Abre archivo txt
    archivotxt = open(rutatxt, "r")

    for linea in archivotxt:
        if len(linea) > 1:
            guardar(archivodat, linea)

    cerrar(archivodat)


def limpiar(archivo):
    try:
        archivo.clear()
        return True
    except Exception:
        raise Exception
