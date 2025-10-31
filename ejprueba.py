nombre="lucia"
nombre.replace("a","o")
print(nombre)
nombre=nombre.replace("a","o")
nombrelista=list(nombre)
nombrelista.insert(0,"A")
print(nombrelista)
cadenasalida=""
for valor in nombrelista:
    cadenasalida+=valor
print(cadenasalida)