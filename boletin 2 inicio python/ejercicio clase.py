dia = input("dame dia de la semana:")
match dia:
    case "lunes"|"martes"|"miercoles"|"jueves"|"viernes":
        print ("clase")
    case "sabado"|"domingo":
        print("casa")
    case _:
        print("no valido")
print("fin")