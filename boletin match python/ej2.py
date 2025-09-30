dia = input("dime un dia:")
dia = dia.upper()
match dia:
    case "MARTES":
        print("---------------")
        print("---------------")
        print("     MARTES     ")
        print("---------------")
        print("---------------")
        print("8-9 FOL")
        print("9-10 EDE")
        print("10-11 PROG")
        print("11-11:30 recre")
        print("11:30-12 PROG")
        print("12-14 BBDD")
    case "Sabado"|"sabado"|"Domingo"|"domingo":
        print("dia de estudio y reflexion")
    case _:
        print("valor incorrecto")
