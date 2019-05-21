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


# ej3  SIEMPRE MUESTRA QUE NO ES PALINDROMO
palabra = 'neuquen'
for elemento in palabra:
    arribo(c, elemento)
print(c.datos)
while not cola_vacia(c):
    dato = atencion(c)
    apilar(p, dato)
invertir(p, p1)
print(p1.datos)
flag = False
while not pila_vacia(p):
    aux = desapilar(p)
    dat = desapilar(p1)
    if aux == dat:
        
    else:
        flag = False


# ej4
# num = '123456789'
'''cargautomatica1(c)
print(c.datos)
while not cola_vacia(c):
    aux = atencion(c)

print(c1.datos)'''


# ej5
'''cargautomatica1(c)
while not cola_vacia(c):
    dato = atencion(c)
    apilar(p, dato)
print(p.datos)
invertir(p, p1)
print(p1.datos)'''
