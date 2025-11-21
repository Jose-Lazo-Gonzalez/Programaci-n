matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]

def pares(matriz):
    suma=0
    for i in range(0,len(matriz)):
        if i%2==0:
            for a in matriz[i]:
                suma+=a
    return suma
print (pares(matriz))