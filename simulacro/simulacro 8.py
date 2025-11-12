impares=[]
contaimpar=0
num1=int(input("introduce un numerin:"))
num2=int(input("introduce otro numerin"))
while num1>=num2:
    num1=int(input("introduce un numerin:"))
    num2=int(input("introduce otro numerin"))
if num1<num2:
    a=input("el rango es abierto o es cerrado")
    if a=="cerrado":
        while num1 !=0 and num2!=0:
            for i in range(num1,num2+1):
                if i%2==1:
                    impares.append(i)
                    
                    contaimpar+=1
                    
            print("=========================================================")
            print(f"Impares que existen entre {num1} y el {num2}:{impares} ")
            print(f"En total existen {contaimpar} números impares en el rango.")
            print("=========================================================")
            num1=int(input("introduce un numerin:"))
            num2=int(input("introduce otro numerin"))
    if a=="abierto":
        while num1 !=0 and num2!=0:
            for i in range(num1+1,num2):
                if i%2==1:
                    impares.append(i)
                    contaimpar+=1
                    
            print("=========================================================")
            print(f"Impares que existen entre {num1} y el {num2}:{impares} ")
            print(f"En total existen {contaimpar} números impares en el rango.")
            print("=========================================================")
            num1=int(input("introduce un numerin:"))
            num2=int(input("introduce otro numerin"))
print("finalizar el programa")