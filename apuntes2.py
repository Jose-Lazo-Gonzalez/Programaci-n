a = "Hello, World"
print(a[1])  # acceder a un carácter mediante su posición (e)

mensaje9 = "Hola Mundo"
mensaje9a = mensaje9[1:8]  # genera una nueva cadena desde la posición inicial (incluida) hasta la posición final (excluida). "ola Mun"

mensaje1 = 'Hola' + ' ' + 'Mundo' # Une dos o más cadenas usando el operador +. "Hola Mundo"
len(mensaje1)  # devuelve el número de caracteres de la cadena (incluidos espacios). (10)
for x in "banana":
  print(x) #imprime cada letra

txt = "The best things in life are free!"
print("free" in txt)  # devuelve True or False si está o no en el txt
print("expensive" not in txt)

mensaje5 = "Hola Mundo" 
mensaje5a = mensaje5.find("Mundo") # find(): Busca la subcadena. Devuelve el índice de inicio de la primera aparición de la subcadena.
                                   # Si lo encuentra, devuelve un número >= 0. Si no lo encuentra, devuelve -1. (5)
print(mensaje5a)

mensaje8 = "HOLA MUNDO LOS LUNES"
mensaje8 = mensaje8.replace("L", "pizza") #cambia las L por "pizza" "HOpizzaA MUNDO pizzaOS pizzaUNES"
print(mensaje8)                           # las cadenas son inmutables, por lo que si pongo sólo mensaje.replace(algo) NO CAMBIA


mensaje2a = 'Hola ' * 3 # Repite la cadena el número de veces especificado. "hola hola hola"
mensaje8.lower() # pasar a minúsculas
mensaje8.upper() # pasar a mayúsculas

txt = "Bienvenidos,a,la,clase,de,programación"
lista = txt.split(',') # (split): Devuelve una lista de cadenas, dividiendo la cadena original en cada aparición del separador (',' en este caso)
['Bienvenidos', 'a', 'la', 'clase', 'de', 'programación'] # resultado

s = "Esto es una comilla doble \" de ejemplo" # las cadenas se crean con comillas pero como no sabe dónde termina, se pone \
print(s)

nombre = "elena"
print(nombre)
nombre = list(nombre) # para convertir una cadena(str) a lista [] 
print(nombre) 
nombre.insert(0,"A") #si quiero utilizar comandos para las listas en cadenas, tengo que convertir a lista
print (nombre)
cadenasalida = ""
for valor in nombre: #paso de lista [] a cadena (str)
  cadenasalida = cadenasalida + valor
print(cadenasalida)