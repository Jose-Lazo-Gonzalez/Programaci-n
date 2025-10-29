
numeros = []
print("Introduce 15 números:")
for i in range(15):
    num = int(input("Que numero te gustaria añadir:"))
    numeros.append(num)



rotada_una = [numeros[-1]] + numeros[:-1]

print("\nLista rotada una posición:")
print(rotada_una)

n = int(input("\nIntroduce el número de rotaciones (debe ser menor que 15): "))

while n >= len(numeros):
    n = int(input("Número inválido. Introduce un número menor que 15: "))


rotada_n = numeros[-n:] + numeros[:-n]

print(f"\nLista rotada {n} veces:")
print(rotada_n)
