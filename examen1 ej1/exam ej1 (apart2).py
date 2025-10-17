import random
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
if menu ==1:
    print("Ejecutando y seleccionando casa")
    nombre=input("introduce el nombre del alumno:")
    casa= random.randint(1,4)
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