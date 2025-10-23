import random
lista=[]
impares=[]
pares=[]
for i in range(20):
    a=random.randint(0,100)
    lista.append(a)
pares = [num for num in lista if num % 2 == 0]
impares = [num for num in lista if num % 2 == 1]
lista=impares
lista+=pares
print(lista)