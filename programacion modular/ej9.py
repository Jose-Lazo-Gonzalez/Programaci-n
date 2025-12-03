matriz=[[8,1,6],
        [3,5,7],
        [4,9,2]]



def devuelvediagonal (matriz):
        linea=0
        posi=0
        lista=[]
        for i in range (len(matriz)):
            lista.append(matriz[linea][posi])
            linea+=1
            posi+=1
        return lista
print(devuelvediagonal(matriz))

def otradiagonal(matriz):
        linea=0
        posi=len(matriz)-1
        lista=[]
        for i in range(len(matriz)):
            lista.append(matriz[linea][posi])
            linea+=1
            posi-=1
        return lista
print(otradiagonal(matriz))