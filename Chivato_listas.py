lista = []
lista = list()  #Crea una lista vacía
lista = [0]  #La posición 0 es la primera de la lista
lista = [-1]  #La posición -1 es la última de la lista
import random  #Importamos algo, en este caso "random"
algo = 0  #Crea una variable
otracosa = 1  #Crea otra variable
suma = algo+otracosa  #Crea una variable sumando, restando... otras variables
#Se puede hacer con listas
lista2 = []
lista3 = lista2+lista  #Así concatenas 2 listas para juntarlas en una
lista.extend(["paquito", False]) #para concatenar listas tambien
len(lista)  #Longitud de la lista
lista.append()  #Añade un elemento al final de la lista
lista.insert()  #Añade un elemento en la posición especificada, por ejemplo: lista.insert(0, 3), añade un 3 en la posición 0
lista.remove()  #Borra un elemento de la lista, por ejemplo: lista.remove(Laura), borra el Laura de la lista
lista.pop()  #Borrapor defecto el útimo elemento de la lista a menos que indiques la posición, es decir, borra por posicion
lista.reverse()  #Reversa el orden de la lista
lista.sort()  #Ordena los elementos de menor a mayor
print(lista.index(2))  #Devuelve en que posición está el primer 2
for i in lista #recorrre la lista, siendo i cada valor de la lista en cada iteracion
lista[1:4]#acota la lista por posiciones, siendo la primera por la que empieza y la segunda por la que acaba

mensaje="Hola Mundo"
mensaje1=mensaje.find("Mundo") #Encontrar algo en una cadena
#Puedo acceder a un carácter mediante su posición
a = "Hello, World!"
print(a[1])
#Generar una subcadena:
mensaje9 = "Hola Mundo"
mensaje9a = mensaje9[1:8]
#Concatenar cadenas  
mensaje1 = 'Hola' + ' ' + 'Mundo'
#Longitud de una cadena 
len(mensaje2a) 
#Recorrer los caracteres de una cadena:
for x in "banana":
  print(x)
#Operador in (devuelve booleano)
txt = "The best things in life are free!"
print("free" in txt)
#Operador not in
print("expensive" not in txt)
#Reemplazar una parte de la cadena:
mensaje8 = "HOLA MUNDO"
mensaje8a = mensaje8.replace("L", "pizza")

mensaje8 = "HOLA MUNDO LOS LUNES"
mensaje8a = mensaje8.replace("L", "pizza") 

#Reemplaza todas las L

#Multiplicar cadenas  
mensaje2a = 'Hola ' * 3
#Pasar a minúsculas  
mensaje8.lower()
#Pasar a mayúsculas  
mensaje8.upper()

#Generar una lista a partir de una cadena:
txt = "Bienvenidos a la clase de programación"

lista = txt.split() # por defecto separa por espacios

['Bienvenidos', 'a', 'la', 'clase', 'de', 'programación']

#string.split(separator, maxsplit)
#Así puedo definir cómo separar y qué máximo de separaciones quiero hacer. Por defecto, serían todas las ocurrencias

#Generar una lista a partir de una cadena:
txt = "Bienvenidos,a,la,clase,de,programación"

lista = txt.split(',') # En este caso el separador es la coma

['Bienvenidos', 'a', 'la', 'clase', 'de', 'programación']

s = "Esto es una comilla doble \" de ejemplo"



