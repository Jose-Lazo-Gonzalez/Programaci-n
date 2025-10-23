import random
lista=[]
cuadrado=[]
cubo=[]
for i in range(20):
    a=random.randint(0,100)
    lista.append(a)
for o in lista:
    cuadrado.append(o**2)
    cubo.append(o**3)

for o in range(20):
    num=(lista[o])
    cua=(cuadrado[o])
    cub=(cubo[o])
    print(num, cua, cub, sep='\t\t')