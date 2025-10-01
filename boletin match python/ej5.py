print("[1] habitacion azul")
print("[2] habitacion roja")
print("[3] habitacion verde")
print("[4] habitacion rosa")
print("[5] habitacion gris")
a = int(input("selecciona una habitacion"))
if a>5 or a<1:
    print("no valido")
    a = int(input("selecciona una habitacion"))
match a:
    case 1:
        print("2 camas")
        print ("primera planta")
    case 2:
        print ("1 cama")
        print ("primera planta")
    case 3:
        print("3 camas")
        print(" segunda planta")
    case 4:
        print ("2 camas")
        print ("segunda planta")
    case 5:
        print(" 1 cama")
        print("tercera planta")
    case _:
        print("no")