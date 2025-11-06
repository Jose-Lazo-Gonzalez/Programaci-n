cadena=input("dame un nombre y apellidos")
cadenasepa=cadena.split(' ')
a="a"
b="b"
c="c"
for i in cadenasepa:
    if a=="a":
        a=i[0]
        f=a.upper()
    elif b=="b":
        b=i[0]
        g=b.upper()
    elif c=="c":
        c=i[0]
        h=c.upper()
print("tus iniciales son:",f,g,h)
