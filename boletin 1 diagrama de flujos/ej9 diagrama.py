a = int(input("dime un numero:"))
b = int(input("dime otro numero:"))
if a>0 and b>0:
    print("hay dos positivos")
elif a<0 and b >0:
    print("hay un positivo")
elif a>0 and b<0:
    print("hay un positivo")
elif a<0 and b<0:
    print("no hay positivos")