lista=[]
for i in range(0,10):
    a=int(input("dame un numero"))
    lista.append (a)

maximo = 0
minimo = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

for i in lista[0:]:
    if i > maximo:
        maximo = i
    if i < minimo:
        minimo = i

print("La lista es:",lista)
print("El valor máximo es:", maximo)
print("El valor mínimo es:",minimo)