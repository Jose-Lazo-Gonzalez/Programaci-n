dia = input("dame dia de la semana:")
match dia:
    case "L"|"M"|"J"|"V":
        print ("clase")
    case "S"|"D":
        print("casa")
    case _:
        print("no valido")
print("fin")