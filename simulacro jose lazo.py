#Ejercicio simulacro
nombre=input("escribe tu nombre:")
while nombre!="exit":
    nota=int(input("introduce tu nota"))
    while nota<0 or nota>100:
        print("error")
        nota=int(input("introduce tu nota"))
    if 90<nota<100:
        print("sobresaliente")
    elif 70<nota<89:
        print("notable")
    elif 60<nota<69:
        print("bien")
    elif 50<nota<59:
        print("suficiente")
    else:
        print("suspenso")
    nombre=input("escribe tu nombre:")



