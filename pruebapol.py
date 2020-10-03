import polinomio
from random import randint

p1 = polinomio.crear(randint(0, 5))
p2 = polinomio.crear(randint(0, 5))
for i in range(0, polinomio.grado(p1)+1):
    polinomio.cargar(p1, i, randint(0, 3))
for i in range(0, polinomio.grado(p2)+1):
    polinomio.cargar(p2, i, randint(0, 3))

print(p1)
print(p2)

polinomio.suma(p1, p2)
print(polinomio.suma(p1, p2))

polinomio.producto(p1, p2)
print(polinomio.producto(p1, p2))
