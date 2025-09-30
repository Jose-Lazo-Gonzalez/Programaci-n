a = int(input("introduce el historial crediticio"))
b = int(input("los años que llevas trabajando"))
c =int(input("sueldo anual"))
d=int(input("prestamo a pedir"))
if a<0:
    print("riesgo a considerar")
elif b<=2:
    print("riesgo a considerar")
elif d>c/100:
    print("riesgo a considerar")
else:
    print("persona valida")