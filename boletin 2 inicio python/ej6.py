print("bienvenido al cajero")
a=int(input("introduce tu saldo:"))
b=int(input("introduce la cantidad de dinero a extraer:"))
if b<=a:
    print("extrayendo dinero...")
else:
    print("no hay saldo suficiente")
print("apagando cajero...")