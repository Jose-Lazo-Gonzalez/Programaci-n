import random
nombre=""
c1=0
c2=0
c3=0
c4=0
while nombre!="voldemort":
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    print("SOMBRERO SELECCIONADOR")
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    print("1. Selecciona casa para un alumno")
    print("2.Mostrar estadisticas")
    print("Elige una opción. Si quieres salir del programa, escribe la opcion 1 y el nombre del personaje innombrable")
    menu=int(input("Selecciona una opcion"))
    while menu!=1 and menu!=2:
        menu=int(input("Selecciona una opcion"))
    if menu ==1 :
        print("Ejecutando y seleccionando casa")
        nombre=input("introduce el nombre del alumno:")
        casa= random.randint(1,4)
        match casa:
            case 1:
                c1+=1
            case 2:
                c2+=1
            case 3:
                c3+=1
            case 4:
                c4+=1
        total=(c1+c2+c3+c4)
        if nombre!="voldemort":
            if casa==1:
                casa="Gryffindor"        
            elif casa==2:
                casa="Slytherin"
            elif casa==3:
                casa="Hufflepuff"
            elif casa==4:
                casa="Ravenclaw"
            print("El sombrero dice que,",nombre,"pertenece a",casa)
        


    if menu ==2:
        print("Ejecutando y mostrando estadisticas")
        print("el total de alumnos es:",total)
        print("Gryffindor:",c1)
        print("Slytherin:",c2)
        print("Hufflepuf:",c3)
        print("Ravenclaw:",c4)
print("Aparrition, transportame a otro sitio")
