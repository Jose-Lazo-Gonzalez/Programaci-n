a =int(input("introduce el numero de filas"))
b="*"
c="#"
for i in range(1,a+1,1):
    if i==1 or i== (a):
        print(b+c*(a-2) + b)
    
    else:
        print(b*a) 