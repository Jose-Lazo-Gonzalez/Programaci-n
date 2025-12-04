numero=input("Introduce el numero que quieres redondear")
listanum=[]
def redondea (listanum, numero):
    for a in numero:
        a=int(a)
        listanum.append(a)
    for i in range (len(numero)-1,-1,-1):
        if listanum[i]>=5:
            listanum[i]=0
            listanum[i-1] = listanum[i-1] + 1
    return listanum
print(redondea(listanum,numero))