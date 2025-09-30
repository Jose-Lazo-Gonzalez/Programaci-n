opcion = input("dame opcion(a,b o c)")
match opcion:
    case "a":
        print("alta")
    case "b":
        print("baja")
    case "c":
        print("cambio")
    case _:
        print("no valido")
print("fin")