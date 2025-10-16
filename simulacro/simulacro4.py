n1=int(input("dame un numero"))
n2=int(input("Dame la segunda cifra"))
n3=int(input("dame la tercera cifra"))
print(n1,n2,n3)
total=0
media=0
numero=0
while n1!=0 or n2 !=0 or n3 !=0:
    if n3>n2>n1:
        print("creciente")
    elif n3<n2<n1:
        print("decreciente")
    else:
        print("desordenado")
    n1=int(input("dame un numero"))
    n2=int(input("Dame la segunda cifra"))
    n3=int(input("dame la tercera cifra"))
    print(n1,n2,n3)
    total+=(n1+n2+n3)
    numero+=3
media=total//numero
print("el total de numeros es",numero)
print("la media es",media)
print("saliendo...")