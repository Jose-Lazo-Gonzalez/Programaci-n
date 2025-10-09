a =int(input("introduce el numero de filas"))
b="*"
c="#"
d="@"
for i in range(a):
    if i%2==0:
        print(b+c*(a-2) + b)
    
    else:
        linea = ""
        for x in range(a):
            if x % 2 == 0:
                linea += "*"
            else:
                linea += "@"
        print(linea)
    
