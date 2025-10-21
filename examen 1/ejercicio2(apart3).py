#nh=numero humano y nm=numero maquina ph=apuesta humana 
import random
nh=int(input("cuantas piedras quieres mostrar?:"))
nm= random.randint(0,5)
while (0<=nh<=5)== False:
    print("error")
    nh=int(input("cuantas piedras quieres mostrar?:"))
ph=input("porque deseas apostar? par(P)/impar(I)")
ganadasjugador=0
ganadasmaquina=0

c0=0
c1=0
c2=0
c3=0
c4=0
c5=0
while nh!=nm:
    match nh:
        case 0:
            c0+=1  
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

    print("la maquina eligio:",nm)
    print("el numero total es",nh+nm)
    if (nh+nm)%2==0 and ph=="P":
        print("has ganado")
        ganadasjugador+=1
    elif (nh+nm)%2==0 and ph=="I":
        print("has perdido, maquina ganadora")
        ganadasmaquina+=1
    elif (nh+nm)%2==1 and ph=="P":
        print("has perdido, maquina ganadora")
        ganadasmaquina+=1
    elif (nh+nm)%2==1 and ph=="I":
        print("has ganado")
        ganadasjugador+=1
    nh=int(input("cuantas piedras quieres mostrar?:"))
    nm= random.randint(0,5)
    while (0<=nh<=5)== False:
        print ("error")
        nh=int(input("cuantas piedras quieres mostrar?:"))
    ph=input("porque deseas apostar? par(P)/impar(I)")
print("fin")
print("la maquina ha ganado:",ganadasmaquina)
print("el jugador ha ganado:",ganadasjugador)
numerototal=(ganadasjugador+ganadasmaquina)
print("el total de partidas ha sido:",numerototal)
if c1>c2 and c1>c3 and c1>c4 and c1>c5 and c1>c0:
    print ("el mas frecuente es 1")
elif c2>c1 and c2>c3 and c2>c4 and c2>c5 and c2>c0:
    print ("el mas frecuente es 2")
elif c3>c2 and c3>c1 and c3>c4 and c3>c5 and c3>c0:
    print ("el mas frecuente es 3")
elif c4>c2 and c4>c3 and c4>c1 and c4>c5 and c4>c0:
    print ("el mas frecuente es 4")
elif c5>c2 and c5>c3 and c5>c4 and c5>c1 and c5>c0:
    print ("el mas frecuente es 5")
elif c0>c2 and c0>c3 and c0>c4 and c0>c5 and c0>c1:
    print ("el mas frecuente es 0")






