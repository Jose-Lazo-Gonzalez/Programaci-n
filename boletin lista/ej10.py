
numeros = []
print("Introduce 15 números:")
for i in range(15):
    num = int(input("dame un numero:"))
    numeros.append(num)
rotado = [numeros[-1]] + numeros[:-1]
print("Lista rotada una posición:")
print(rotado)
n = int(input("Introduce el número de rotaciones "))
while n >= len(numeros):
    n = int(input("Número inválido. Introduce un número menor que 15: "))
rotada = numeros[-n:] + numeros[:-n]

print(rotada)
