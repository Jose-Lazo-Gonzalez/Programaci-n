def obtieneYValidaDatosDeEntrada ():
    a=int(input("dame un numero positivo"))
    while a<0:
        a=int(input("dame un numero positivo"))
    return a

entrada=obtieneYValidaDatosDeEntrada()
print(entrada)