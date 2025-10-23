import random

lista = []
cuadrados = []
cubos = []
n_elementos = 20

# 1. Generar la lista de 20 números aleatorios
for i in range(n_elementos):
    a = random.randint(0, 100)
    lista.append(a)

# 2. Calcular los cuadrados y cubos
for n in lista:
    cuadrados.append(n ** 2)
    cubos.append(n ** 3)

# 3. Mostrar el contenido en tres columnas usando el separador de print()

# Imprimir cabeceras (aquí los títulos SÍ deben ser cadenas)
print("Números", "Cuadrados", "Cubos", sep='\t\t')
print("-------------------------------------------------")

# Usar el índice para acceder a las tres listas
for i in range(n_elementos):
    num = lista[i]
    cuad = cuadrados[i]
    cubo = cubos[i]

    # Imprimir los datos: print() acepta argumentos de tipo entero.
    # El argumento 'sep' se encarga de convertir y separar los datos.
    # Usamos '\t\t' y '\t' estratégicamente para la alineación.
    print(num, cuad, cubo, sep='\t\t') # Nota: la tabulación doble se aplica entre