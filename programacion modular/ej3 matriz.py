matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]

def pares(matriz):
    par=[]
    for i in matriz:
        for a in i:
            if a%2==0:
                par.append(a)
    return par
print(pares(matriz))