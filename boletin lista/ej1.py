listaanimal=["gato","perro","gallina","raton"]
a=input("dime un animal para buscar en el zoo:")
while listaanimal==["gato","perro","gallina","raton"]:
    if a in listaanimal:
        print("lo encontre")
        print(listaanimal.index(a))
    else:
        print("no hay")
        print(listaanimal)
        print(listaanimal[1:3])
    a=input("dime un animal para buscar en el zoo:")