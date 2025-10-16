año=int(input("dime un año:"))
while año>=0:
    if año%400==0:
        print("es año bisiesto")
    elif año%100==0:
        print("no es año bisiesto")
    elif año%4==0:
        print("es año bisiesto")
    else:
        print("no es año bisiesto")
    año=int(input("dime un año:"))
print("fin del programa")