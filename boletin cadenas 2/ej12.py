#Escribir un programa que reciba una cadena que contiene un número entero y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe 1234567890, debe devolver 1.234.567.890.
cadena=input("dame un numero")
vacia=""
contador=0
for i in range(len(cadena)-3,0,-3):
    print(cadena[i:i+3])
    vacia=cadena[contador-len(cadena)]+"."+(cadena[i:i+3])+vacia
    contador+=3
print (vacia)