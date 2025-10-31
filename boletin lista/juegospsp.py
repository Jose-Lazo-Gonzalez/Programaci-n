opcion=""
nombre=[]
puntuaciones=[]
generos=[]
busqueda=[]
while opcion!="S":
    print("Selecciona una de las siguientes opciones (R, E, S, P) ")
    print("R. Registrar juegos")
    print("E. Mostrar estadísticas")
    print("P. Cual tiene mayor puntuacion")
    print("D.Detalles de un juego:")
    print("G.Filtrar por genero:")
    print("S. Salir del programa:")
    opcion=input("selecciona una opcion:").upper()
    while  opcion!="S":
        if opcion=="R":
            a=int(input("cuantos juegos quieres registrar:"))
            for i in range (a):
                    game=input("nombre del juego:")
                    punt=input("puntuacion del juego:")
                    gen=input("genero del juego:")
                    nombre.append(game)
                    puntuaciones.append(punt)
                    generos.append(gen)
        
        elif opcion=="E":
            for o in range(0,len(nombre)):
                num=(nombre[o])
                cua=(puntuaciones[o])
                cub=(generos[o])
                print(num, cua, cub, sep='\t\t')

        elif opcion=="P":
            maximo = puntuaciones[0]
            for i in puntuaciones[0:]:
                if i > maximo:
                    maximo = i
            posicion=puntuaciones.index(maximo)
            print(nombre[posicion], puntuaciones[posicion],generos[posicion])
        
        elif opcion=="D":
            b=input("escribe el nombre para ver los detalles:")
            if b in nombre:
                n=nombre.index(b)
                print(nombre[n],puntuaciones[n],generos[n])
            else:
                print("no se encuentra en la base de datos")
        
        elif opcion=="G":
            k=input("escribe el genero para ver los juegos:")
            
        opcion=input("selecciona una opcion").upper()
    print("Salir del programa:")
            
