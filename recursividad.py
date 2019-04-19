def fib(n):
    if n == 0 or n == 1:
        return(n)
    else:
        return(fib(n-1)+fib(n-2))


def sumar(num):
    if num == 0:
        return(0)
    else:
        return(sumar(num-1)+num)


def producto(n, m):
    if m == 1:
        return(n)
    else:
        return(n + producto(n, m-1))


def potencia(n, m):
    if m == 0:
        return(1)
    else:
        return(n*potencia(n, m-1))


def invertir(cad):
    if len(cad) == 1:
        return(cad)
    else:
        return(cad[len(cad)-1] + invertir(cad[0:len(cad)-1]))


def serie(n):
    if n == 1:
        return(1)
    else:
        return(1/n + serie(n-1))


def convertir(num):
    if num <= 1:
        return(str(num))
    else:
        return(convertir(num//2) + str((num % 2)))


def log(n, b):
    if n <= b:
        return(1)
    else:
        return(1 + log(n/b, b))


def digitos(n):
    if n == 0:
        return(0)
    else:
        return(1+digitos(n//10))


def invnum(n):
    if n < 10:
        return(n)
    else:
        return(((n % 10)*(10**digitos(n//10)))+invnum(n//10))


def euclidesmcd(a, b):
    if b == 0:
        return(a)
    else:
        return(euclidesmcd(b, a % b))


def mcm(a, b):
    if euclidesmcd(a, b) == 1:
        return(a * b)
    else:
        return((a * b) / (euclidesmcd(a, b)))


def sumdig(n):
    if n == 0:
        return(0)
    else:
        return((n % 10) + sumdig(n//10))


def raiz(i, n):
    if (i+1) * (i+1) > n:
        return(i)
    else:
        return(raiz(i + 1, n))


def mat(matriz, i, j):
    if (i >= 0 and j >= 0):
        print(matriz[i][j])
        if j == 0:
            i -= 1
            j = len(matriz[i])
        mat(matriz, i, j-1)


def quicksort(vec, pri, ult):
    i = pri
    j = ult - 1
    pivote = ult
    while i < j:
        while vec[i] <= vec[pivote] and i < j:
            i = i + 1
        while vec[j] > vec[pivote] and j > i:
            j = j - 1
        if i < j:
            vec[i], vec[j] = vec[j], vec[i]
    if vec[i] > vec[pivote]:
        aux = vec[i]
        vec[i] = vec[pivote]
        vec[pivote] = aux
    if pri < i:
        quicksort(vec, pri, j-1)
    if ult > i:
        quicksort(vec, i+1, ult)
    return(vec)


def bbin(vec, pri, ult, busc):
    if pri <= ult:
        med = (pri + ult)//2
        if vec[med] == busc:
            return(med)
        else:
            if vec[med] > busc:
                return(bbin(vec, pri, med - 1, busc))
            else:
                return(bbin(vec, med + 1, ult, busc))
    else:
        return(-1)


lab1 = [[1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 2]]


def laberinto(lab, x, y, camino):
    f = len(lab)
    c = len(lab)
    if ((x >= 0 and x < f) and (y >= 0 and y < c)):
        if (lab[x][y] == 2):
            camino.append([x, y])
            print("saliste")
            print(camino)
        elif (lab[x][y] == 1):
            lab[x][y] = 3
            camino.append([x, y])
            laberinto(lab, x, y + 1, camino)
            laberinto(lab, x, y - 1, camino)
            laberinto(lab, x + 1, y, camino)
            laberinto(lab, x - 1, y, camino)
            camino.pop()
            lab[x][y] = 1


def torrehanoi(n, inc='1', med='2', fin='3'):
    if n > 0:
        torrehanoi(n-1, inc, fin, med)
        print('se mueve de torre', inc, 'a torre', fin)
        torrehanoi(n-1, med, inc, fin)


def sucesion(n):
    if n == 1:
        return(3)
    else:
        return((sucesion(n - 1) + 2))
