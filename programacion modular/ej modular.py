cadena=input("introduce una cadena de mas de 4 caracteres")
concadenacion=""
cadena7="0"
while len(cadena) < 4:
    cadena=input("introduce una cadena de mas de 4 caracteres")
def calcula(numero,posic1,posic2):
    salida=numero[posic1]+numero[posic2]
    return salida
num=int(cadena)
if   num%2==0:
        output=calcula(cadena,1,3)
        print(output)
elif num%3==0:
        output=calcula(cadena,1,2)
        print(output)
elif num%7==0:
        output=calcula(cadena,0,3)
        print(output)
