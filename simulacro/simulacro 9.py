num=int(input("introduce el numero de arboles que va a introducir:"))
c1=0
c2=0
c3=0
edadmedia=0
alturamax=0
for i in range (num):
    c1+=1
    tipo=input(f"introduce el tipo de arbol para el arbol {c1}:").upper()
    diametro=int(input(f"introduce el diametro del arbol {c1}"))
    altura=int(input(f"introduce la altura del arbol {c1}"))
    if i==0:
        alturamin=altura
    if altura>alturamax:
        alturamax=altura
    if altura<alturamin:
        alturamin=altura
    if tipo=="B":
        edad=int(input(f"introduce la edad del arbol {c1}"))
        c2+=1
        edadmedia+=edad
    if altura>30:
            c3+=1
print(f"La altura maxima es {alturamax}")
print(f"La altura minima es {alturamin}")
print(f"La media de edad para los tipo B es de {edadmedia//c2}")
print(f"Existen {c3} arboles de mas de 30 metros")
        

    