###listas####
milista = [35, 24, 62, 52, 30, 30, 17]
miotralista = ["ismael" ,21 , 1.92 , "ruiz"]
#print (miotralista)

#print(len(milista))

#print(milista)

#print(miotralista [0]) #nos printea el elemento en el indice de ese numero, en este caso 35
#print(miotralista [1])
#print(miotralista [-1]) nos printea el elemento marcado, en este caso al ser un - empieza por el final 
#print(miotralista [-3])

print(milista.count(30))

#nombre, edad, altura, apellido = miotralista
#print(edad)



milista.append("IsmaelA") #añade un valor AL FINAL de la lista
print(milista)

milista.insert(1, "IsmaelB") #inserta un valor en la posicion que quieras marcandola primero y luego poniendo el valor
print(milista)


milista.remove("IsmaelB") #borra el valor indicado, si el valor esta duplicado borra el primero a la izquierda 
print(milista)

milista.pop()#deslista el ultimo elemento y si hacemos un print nos indica cual
print(milista)

milista.pop(1)#deslista el elemento indicado en el indice, el elemento "borrado" lo podemos guardar con una variable
print(milista)

copia_de_mi_lista = milista.copy() #nos crea una nueva lista con el mismo contenido de la lista despues del = 
print(copia_de_mi_lista)

milista.clear()#limpia la lista
print(milista)

copia_de_mi_lista.reverse()#nos da la vuelta a la lista 
print(copia_de_mi_lista)

copia_de_mi_lista.sort()#ordenar la lista, se le pueden dar criterios de la forma que quieras

::-1