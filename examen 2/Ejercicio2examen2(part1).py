

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
elif opcion=="J":
    print("Jugando...")
elif opcion=="E":
    print("saliendo")