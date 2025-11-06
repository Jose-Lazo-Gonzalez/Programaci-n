cadena=input("escrieme algo:")
c1=input("escribeme un caracter")
c2=input("escribeme otro caracter")
if c1 in cadena:
    cadenamod=cadena.replace(c1,c2)
    print(cadenamod)
else:
    print("que va tronco, no hay c1 en la cadena")