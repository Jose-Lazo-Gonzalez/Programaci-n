import random
cminas=0
opcion="T"
while opcion!="E":
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
        tablero=[]
        for i in range(8):
                rd=random.randint(0,1)
                if rd==1:
                    tablero.append("X")
                    cminas+=1
                elif rd==0:
                    tablero.append(" ")
        print(f"¡Tablero Generado! Se han escondido {cminas} minas. Tablero: {tablero}")
    elif opcion=="J":
        print("Jugando...")
    elif opcion=="E":
            print("saliendo")