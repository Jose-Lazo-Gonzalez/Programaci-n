matriz=[[8,2,8],
        [3,5,7],
        [4,9,2]]
def suma (matriz ):
    resultado=0
    for i in range(len(matriz)):
        for a in range (len(matriz[i])):
            if a%2==0:
            
                    resultado+=matriz[i][a]
            
        

    return resultado
print (suma(matriz ))