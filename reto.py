jilguero=[]
cuenta=1
notalist=[]
nota=5
c1=0
c2=0
c3=0
c4=0
c5=0
def calculaLista():
    while nota>0:
        nota=int (input ("introduce la nota del jilguero"))
        notalist.append(nota)
        jilguero.append(cuenta)
        match nota:
                case 1:
                    c1+=1
                case 2:
                    c2+=1
                case 3:
                    c3+=1
                case 4:
                    c4+=1
                case 5:
                    c5+=1
    notalist.pop()
    return notalist, c1,c2,c3,c4,c5
def repes (c1,c2,c3,c4,c5):
    if c1>1 or  c2>1 or  c3>1 or  c4>1 or  c5>1 :
        a=" repes no es valida"
    else:
        a="repes si es valida"
    return a
def mucho(notalist):
    maxi=max(notalist)
    mini=min(notalist)
    listacorrecta=[]
    for i in range (mini, maxi+1, 1):
        listacorrecta.append(i)
    if notalist==listacorrecta:
        b=" maximo es valido"
    else:
        b=" maximo no es valido"
    return b
def calculapuntos(notalist):
    puntos=len(notalist)
    return puntos

print(mucho(notalist))   
print (repes(c1,c2,c3,c4,c5))
if repes(c1,c2,c3,c4,c5)=="repes no es valida" or mucho(notalist)=="maximo no es valido":
    print ("puntuacion:",calculapuntos(notalist))