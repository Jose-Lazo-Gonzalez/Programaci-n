mes = int(input("dime el numero de mes:"))
dia = int(input("dime un dia:"))
match mes:
    case 1 | 2 :
        print("invierno")
    case 3:
        if dia<20:
            print("invierno")
        elif dia>20:
            print("primavera")
    case 4 | 5 :
        print("primavera")
    case 6:
        if dia<=20:
            print("primavera")
        elif dia>20:
            print("verano")
    case 7 | 8 :
        print("verano")
    case 9:
        if dia<=20:
            print("verano")
        elif dia >20:
            print("otoño")
    case 10 | 11:
        print("otoño")
    case 12:
        if dia<=20:
            print("otoño")
        elif dia>20:
            print("invierno")
    case _:
        print("no es un mes valido")
    