gastarmax=int(input("Introduce el dinero maximo que te quieres gastar en la compra ($)"))
nombres=[]
precios=[]
total=0
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

