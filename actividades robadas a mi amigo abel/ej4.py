a=int(input("dame un numero"))
contador=0
media=0
total=0
while 0<=a<=10000:
    contador = contador+1
    total+=a
    media = total//contador
    print ("dentro")
    mayor1=a
    if a>mayor1:
        mayor1=a
    a=int(input("dame un numero"))
    
    
    

    
    

print("fuera")
print ("se han introducido",contador)
print("la media es:", media)
print("el mayor es:",mayor1)
