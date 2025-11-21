numeros=[[0,2,4],
        [1,3,5],
        [6,8,10]]
def suma(numeros,resultado ):
    for i in numeros:
            for a in i:
                    resultado+=a
    return resultado
print (suma( numeros,0)) 