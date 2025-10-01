mes = int(input("dime el numero de mes"))
match mes:
    case 1 | 2 | 3:
        print("invierno")
    case 4 | 5 | 6:
        print("primavera")
    case 7 | 8 | 9:
        print("verano")
    case 10 | 11 | 12:
        print("otoño")
    case _:
        print("no es un mes valido")