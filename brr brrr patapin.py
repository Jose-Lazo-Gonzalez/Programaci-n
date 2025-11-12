letra = input("Introduce una letra: ")
lista = []
stop = True # ojito, que sin esto no furula

while len(letra) != 1:
    print("INCORRECTO, SE NECESITA SÓLO UNA LETRA")
    letra = input("Introduce UNA SOLA letra: ") 

while stop:
    list = input("Introduce palatras, introduce STOP si quieres parar: ") .lower()
    if list == "stop":
        stop = False
    else:
        lista.append(list)

print("La letra introducida es: ", letra)
print("La lista de palabras es: ", lista, "y el número de palabras es:", len(lista))

opcion = ""
while opcion != "S":
    print("E: Lista de palabras que comienzan por la letra")
    print("C: Lista de palabras que contienen la letra")
    print("S: Salir del programa")
    opcion = input("Introduce una opción: ") .upper()

    if opcion == "E":  # lógica para palabras que COMIENZAN por la letra
        palabras_inicio = []
        for i in lista: # recorremos la lista
            if i[0] == letra: # primera letra = letra
                if len(i) > 0: # "si las palabras que empiezan por la letra son más que 1..."
                    palabras_inicio.append(i)
        print("Lista: ",palabras_inicio) # imprime la conclusión, aquello a lo que lleva el for
    
    elif opcion == "C":
        cont_lista = []
        for x in lista:
            if letra in x: # si la letra está en alguna palabra de la lista
                cont_lista.append(x)
        print("Lista2: ", cont_lista)
    else:
        print("Inválido")
print("FIN DEL PROGRAMA")