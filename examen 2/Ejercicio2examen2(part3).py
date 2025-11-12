import random
cminas=0
punt=0
opcion="T"
tablero=[]
rest=1
vistas=[]
while opcion!="E" and rest>=1:
    print("T) Pulse T para generar un nuevo tablero:")
    print("J) Pulse J para jugar")
    print("E) Pulse E para salir del juego")
    opcion=input("Elige una opcion:")
    while opcion!="E" and opcion!="T" and opcion!="J":
        print("T) Pulse T para generar un nuevo tablero:")
        print("J) Pulse J para jugar")
        print("E) Pulse E para salir del juego")
        opcion=input("Elige una opcion:")
    if opcion=="T":
        print("generando tablero...")
        for i in range(8):
                rd=random.randint(0,1)
                if rd==1:
                    tablero.append("X")
                    cminas+=1
                elif rd==0:
                    tablero.append(" ")
        print(f"¡Tablero Generado! Se han escondido {cminas} minas. Tablero: {tablero}")
    elif opcion=="J":
        print(f"Jugando..., tienes que encontrar {cminas} minas")
        if len(tablero)>0:
            posic=int(input("Introduce una posicion (0-7):"))
            rest=cminas
            while rest>=1:
                if posic<0 or posic>7:
                    print("Posicion no valida")
                    posic=int(input("Introduce una posicion (0-7):"))
                elif posic in vistas:
                    print("Ya has encontrado esa mina ")
                    posic=int(input("Introduce una posicion (0-7):"))
                elif tablero[posic]=="X":
                    rest-=1
                    punt+=1
                    vistas.append(posic)
                    print(f"MINA +1 punto (Puntuacion:{punt}, Minas restantes:{rest})")
                    posic=int(input("Introduce una posicion (0-7):"))
                    
                elif tablero[posic]==" ":
                    punt-=1
                    print(f"AGUA -1 punto (Puntuacion:{punt}, Minas restantes:{rest})")
                    posic=int(input("Introduce una posicion (0-7):"))
                    

                    
        elif len(tablero)<1:
            print("debes generar un tablero antes de jugar")
        
        print("--FIN DEL JUEGO--")
        print(f"Puntuacion {punt}")
    elif opcion=="E":
            print("saliendo")