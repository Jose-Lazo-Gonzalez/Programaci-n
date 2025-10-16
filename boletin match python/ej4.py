hemisferio=input("dime un hemisferio:")
mes = int(input("dime el numero de mes:"))
dia = int(input("dime un dia:"))
while dia<=31 or mes<=12:
    #me falta la validacion del hemisferio
    if hemisferio == "NORTE":
        match mes:
            case 1 | 2 :
                print("invierno")
            case 3:
                if dia<=20:
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
                if dia<=22:
                    print("verano")
                elif dia >22:
                    print("otoño")
            case 10 | 11:
                print("otoño")
            case 12:
                if dia<=20:
                    print("otoño")
                elif dia>20:
                    print("invierno")
    elif hemisferio == "SUR":
        match mes:
            case 1 | 2 :
                print("verano")
            case 3:
                if dia<=20:
                    print("verano")
                elif dia>20:
                    print("otoño")
            case 4 | 5 :
                print("otoño")
            case 6:
                if dia<=20:
                    print("otoño")
                elif dia>20:
                    print("invierno")
            case 7 | 8 :
                print("invierno")
            case 9:
                if dia<=22:
                    print("invierno")
                elif dia >22:
                    print("primavera")
            case 10 | 11:
                print("primavera")
            case 12:
                if dia<=20:
                    print("primavera")
                elif dia>20:
                    print("verano")
    hemisferio=input("dime un hemisferio:")
    mes = int(input("dime el numero de mes:"))
    dia = int(input("dime un dia:"))

print("no es una fecha valida valido")