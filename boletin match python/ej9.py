import random

apuesta=int(input("introduce 1 para piedra,2 para tijeras y 3 para papel:"))

numero = random.randint(1,3)

match apuesta:
    case 1:
        print ("humano, piedra")
    case 2 :
        print("humano, tijera")
    case 3 :
        print("humano, papel")
    case _:
        print("respuesta no valida")
match numero:
    case 1:
        print ("maquina, piedra")
    case 2 :
        print("maquina, tijera")
    case 3 :
        print("maquina, papel")
    case _:
        print("respuesta no valida")

if apuesta == numero:
    print("empate")
elif apuesta==1 and numero ==2:
    print("gana el humano")
elif apuesta==2 and numero ==3:
    print("gana el humano")
elif apuesta==3 and numero ==1:
    print("gana el humano")
elif apuesta==2 and numero ==1:
    print("gana la maquina")
elif apuesta==3 and numero ==2:
    print("gana la maquina")
elif apuesta==1 and numero ==2:
    print("gana la maquina")
elif apuesta==1 and numero ==3:
    print("gana la maquina")