#nh=numero humano y nm=numero maquina ph=apuesta humana 
import random
nh=int(input("cuantas piedras quieres mostrar?:"))
nm= random.randint(0,5)
while (0<=nh<=5)== False:
    print("error")
    nh=int(input("cuantas piedras quieres mostrar?:"))
ph=input("porque deseas apostar? par(P)/impar(I)")
while nh!=nm:
    print("la maquina eligio:",nm)
    print("el numero total es",nh+nm)
    if (nh+nm)%2==0 and ph=="P":
        print("has ganado")
    elif (nh+nm)%2==0 and ph=="I":
        print("has perdido, maquina ganadora")
    elif (nh+nm)%2==1 and ph=="P":
        print("has perdido, maquina ganadora")
    elif (nh+nm)%2==1 and ph=="I":
        print("has ganado")
    nh=int(input("cuantas piedras quieres mostrar?:"))
    nm= random.randint(0,5)
    while (0<=nh<=5)== False:
        print ("error")
        nh=int(input("cuantas piedras quieres mostrar?:"))
    ph=input("porque deseas apostar? par(P)/impar(I)")
print("fin")