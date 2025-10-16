n=int(input("dame un numerin:"))
suma=0
while n>=0:
    for i in range (2,n):
        suma=i+suma
    print(suma)
    suma=0
    n=int(input("dame un numerin:"))
print("error")
n=int(input("dame un numerin:"))
