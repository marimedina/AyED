from tdacola import cargautomatica1, cola_llena, cola_vacia, arribo, atencion
from tdacola import Cola, mover_al_final, barrido, cargaAutoStr
from tdapila import invertir, apilar, Pila, desapilar, pila_vacia
from tdapila import cargautomatica
c = Cola()
c1 = Cola()
c2 = Cola()
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


# ej6 NO MUESTRA LOS PRINT
cargautomatica1(c)
print(c.datos)
num = 5
cont = 0
while not cola_vacia(c):
    dato = atencion(c)
    if (dato == num):
        cont += 1
        arribo(c, dato)
print('cantidad de ocurrencias: ' + cont)
