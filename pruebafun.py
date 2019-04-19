import recursividad
#ej1
print(recursividad.fib(6))
#ej2
print(recursividad.sumar(5))
#ej3
print(recursividad.producto(3, 2))
#ej4
print(recursividad.potencia(3, 2))
#ej5
print(recursividad.invertir('hola'))
#ej6
print(recursividad.serie(3))
#ej7
print(recursividad.convertir(11))
#ej8
print(recursividad.log(8, 2))
#ej9
print(recursividad.digitos(215))
#ej10
print(recursividad.invnum(397))
#ej11
print(recursividad.euclidesmcd(1331, 1001))
#ej12
print(recursividad.mcm(500, 120))
#ej13
print(recursividad.sumdig(75))
#ej14
print(recursividad.raiz(2, 16))

#ej15
mat = [[1, 2, 3], [4, 5, 6]]
print(recursividad.mat(mat, 1, 2))
#ej16
lista = [-5, 6, 1, 10, -25]
print(recursividad.quicksort(lista, 0, len(lista)-1))
#ej17
v = [1, 2, 7, 9, 25, 27]
print(recursividad.bbin(v, 0, len(v)-1, 7))
#ej18
lab = [[1, 1, 1, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 1, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 1, 1, 2]]
camino = []
print(recursividad.laberinto(lab, 0, 0, camino))
#ej19
print(recursividad.torrehanoi(3))
#ej20
print(recursividad.sucesion(7))
