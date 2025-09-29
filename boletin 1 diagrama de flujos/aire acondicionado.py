temperatura = (float(input("introduce temperatura:")))
if temperatura>26:
    print("encendiendo aire acondicionado")
    temperatura =(float(input("introduce temperatura:")))
    if temperatura<23:
        print("apago el aire")
else:
    print("no encender el aire")
    if temperatura<10:
        print("enciendo la calefaccion")
print ("registro:" + str(temperatura))
