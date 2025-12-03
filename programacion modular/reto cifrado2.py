matriz = [
    ['A', 'B', 'C', 'D'],    # Fila 1
    ['E', 'F', 'G', 'H'],    # Fila 2
    ['I', 'J', 'K', 'L'],    # Fila 3
    ['M', 'N', 'Ñ', 'O'],    # Fila 4
    ['P', 'Q', 'R', 'S'],    # Fila 5
    ['T', 'U', 'V', 'W'],    # Fila 6
    ['X', 'Y', 'Z', '_']     # Fila 7  (“_” representa el espacio)
]
listaseparada=[]
cadena="21,34,74,21,71,31,61,44,74,34,34,21,23,11,74,13,44,42,74,61,53,11,12,11,32,44,74,72,74,51,21,53,54,31,54,61,21,42,13,31,11"
listacadena=cadena.split(",")
for a in listacadena:
    for x in a:
        listaseparada.append(x)
def descifrado(cadena,matriz,listacadena,listaseparada):
    listadescifrada=[]
    linea=[]
    posi=[]
    for i in range (0,len(listaseparada),1):
        if i%2==0:
            linea.append(listaseparada[i])
        else:
            posi.append(listaseparada[i])
    for x in range(0,len(linea),1):
        y=int(linea[x])-1
        z=int(posi[x])-1
        listadescifrada.append(matriz[y][z])
    return listadescifrada
print(descifrado(cadena,matriz,listacadena,listaseparada))

def cifrado(matriz, palabra):
    palabralista=[]
    c1=-1
    palabra=input("dame la palabra a cifrar")
    for i in palabra:
        letra=i
        for a in matriz:
            c1+=1
            posi=a.index(letra)
        
        


