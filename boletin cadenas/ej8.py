numero=input("dame un numero")
cadenasalida=""
numerolista=list(numero)
n=input("que numero quieres introducir")
numerolista.append(n)
for valor in numerolista:
    cadenasalida+=valor
print(cadenasalida)