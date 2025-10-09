a =int(input("introduce el numero de filas"))
b="*"
c="#"
d="@"
for i in range(a):
    if i%2==0:
        print(b+c*(a-2) + b)
    
    else:
        line = ""
        for j in range(a):
            if j % 2 == 0:
                line += "*"
            else:
                line += "@"
        print(line)
    
