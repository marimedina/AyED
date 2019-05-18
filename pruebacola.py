from tdacola import cargautomatica, cola_llena, cola_vacia, arribo, atencion
from tdacola import Cola, mover_al_final, barrido, cargaAutoStr
'''from tdapila import '''
c = Cola()
c1 = Cola()
c2 = Cola()


# ejcarpeta
'''
cargautomatica(c)
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


# ej3




# ej4
cargautomatica(c)
print(c.datos)
while not cola_vacia(c):
    aux = atencion(c)
    if 
