meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
temperatura=[]
contados=0
j=[]
for i in range(0,12):
    temp=int(input("dime la temperatura del mes por orden:"))
    temperatura.append(temp)
    j.append(temp)


for grados in temperatura:
    temperatura[contados]=grados*"*"
    contados+=1

for a in range(0,12):
    print("la temperatura media en:",meses[a],temperatura[a],j[a],"Cº")
