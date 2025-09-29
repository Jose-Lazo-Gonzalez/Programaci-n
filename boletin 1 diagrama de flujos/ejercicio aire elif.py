temperatura = (float(input("introduce temperatura:")))
if temperatura>26:
    print("encendiendo aire acondicionado")
elif temperatura<10:
        print("enciendo la calefaccion")
else:
    print("no encender nada")
print ("registro:" + str(temperatura))