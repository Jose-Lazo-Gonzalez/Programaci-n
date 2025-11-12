gastarmax=int(input("Introduce el dinero maximo que te quieres gastar en la compra ($)"))
nombres=[]
precios=[]
total=0
opcion="o"
while gastarmax>total:
    nom=input("dime el nombre de un producto")
    pre=int(input("dime su precio"))
    total+=pre
    nombres.append(nom)
    precios.append(pre)
total=total-precios[-1]
nombres.pop()
precios.pop()
#resumen
print(f"importe maximo a gastar {gastarmax}")
print(f"Productos: {nombres}")
print(f"Precios: {precios}")
print(f"Coste total de la cesta {total}")

while opcion!="E":
    print("Pulse la opcion S para calcular el dinero sobrante")
    print("Pulse la opcion R para eliminar un producto y su precio de la lista")
    print("Pulse la opcion C para devolver la lista cuyo precio es mas alto que un importe")
    print("E) Salir del programa")
    opcion=input("Eliga una opcion")
    while opcion!="S" and opcion!="R" and opcion!="C" and opcion!="E":
        print("Pulse la opcion S para calcular el dinero sobrante")
        print("Pulse la opcion R para eliminar un producto y su precio de la lista")
        print("Pulse la opcion C para devolver la lista cuyo precio es mas alto que un importe")
        print("Salir del programa")
        opcion=input("Eliga una opcion")
    if opcion=="S":
        print("Sobrante")
        sobra=gastarmax-total
        print(f"Sobra un total de {sobra} euros")
    elif opcion=="R":
        print("Remove")
        print(nombres)
        print(precios)
        nr=input("Dime el nombre de un producto")
        seguridad=input(f"Vas a eliminar el producto con nombre {nr}, estas segura? S/N")
        if seguridad=="S":
            borro=nombres.index(nr)
            nombres.pop(borro)
            precios.pop(borro)
        print(nombres)
        print(precios)
        
    elif opcion=="C":
        print("productos caros")
print("saliendo del programa...")
