matriz=[[8,1,6],
        [3,5,7],
        [4,9,2]]
columna=int(input("dime la columna la cual quieres sumas"))
def suma (matriz, columna):
    resultado=0
    for i in matriz[columna]:
        resultado+=i

    return resultado
print (suma(matriz, columna))