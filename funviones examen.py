lista=[1, 2, 3]
def suma (lista):
    resul=lista[0]+lista[1]
    lista.insert (2,resul)
    return lista

print (lista)