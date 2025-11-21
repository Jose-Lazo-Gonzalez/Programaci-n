matriz=[[8,1,6],
        [3,5,7],
        [4,9,2]]
a=int(input("elige una fila"))
def suma (matriz, a):
    resultado=0
    for i in matriz[a]:
        resultado+=i
    return resultado
print (suma(matriz,a))
