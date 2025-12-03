def Registropuntuaciones(fase):
    inicial = semifinal = final = False
    matriz = []
    c1 = 0

    if fase == "inicial":
        inicial = True
        total = 8
    elif fase == "semifinal":
        semifinal = True
        total = 4
    elif fase == "final":
        final = True
        total = 2

    # Registrar puntuaciones
    for i in range(total):
        nombre = input(f"Dime el nombre del equipo {c1}: ")
        puntos = input(f"Dime los puntos del equipo {c1}: ")
        c1 += 1
        matriz.append([nombre, puntos])

    print("=============================")
    print("Datos registrados correctamente")
    print("=============================")
    print(matriz)

    return matriz, inicial, semifinal, final


def listarPuntuacionesEquipo(fase, datos, inicial, semifinal, final):
    fase_upper = fase.upper()

    fases_info = {
        "INICIAL": (inicial, 8, "Fase Inicial"),
        "SEMIFINAL": (semifinal, 4, "Fase Semifinal"),
        "FINAL": (final, 2, "Fase Final"),
    }

    if fase_upper not in fases_info:
        print("Fase inválida.")
        return

    registrada, cantidad, titulo = fases_info[fase_upper]

    if not registrada:
        print("==========================")
        print(f"La fase {fase} no ha sido registrada")
        print("==========================")
        return

    print("============================")
    print(titulo)
    print("============================")

    for i in range(cantidad):
        print(f"El equipo {datos[i][0]} ha obtenido {datos[i][1]} puntos")


def calculaClasificados(fase, datos, inicial, semifinal, final):
    fase_upper = fase.upper()

    fases_info = {
        "INICIAL": (inicial, 4, "Clasificados Fase Inicial"),
        "SEMIFINAL": (semifinal, 2, "Clasificados Semifinal"),
        "FINAL": (final, 1, "Ganador de la Final"),
    }

    if fase_upper not in fases_info:
        print("Fase inválida.")
        return

    registrada, num_top, titulo = fases_info[fase_upper]

    if not registrada:
        print("==========================")
        print(f"La fase {fase} no ha sido registrada")
        print("==========================")
        return

    print("============================")
    print(titulo)
    print("============================")

    copia = datos.copy()
    top = []

    # Seleccionar mejores puntajes
    for _ in range(num_top):
        max_equipo = None
        max_puntos = -1
        for equipo in copia:
            puntos = int(equipo[1])
            if puntos > max_puntos:
                max_puntos = puntos
                max_equipo = equipo
        top.append(max_equipo)
        copia.remove(max_equipo)

    for equipo in top:
        print(equipo)


# ============================================
#           MENÚ PRINCIPAL
# ============================================

opcion = ""
datos = []
inicial = semifinal = final = False

while opcion != "S":
    print("\n===== MENÚ =====")
    print("R) Registrar puntuaciones")
    print("L) Listar equipos y puntuaciones")
    print("C) Clasificación por fase")
    print("S) Salir")
    opcion = input("Elige una opción: ").upper()

    if opcion == "R":
        fase = ""
        while fase not in ("inicial", "semifinal", "final"):
            fase = input("Di la fase actual (inicial / semifinal / final): ").lower()

        datos, inicial, semifinal, final = Registropuntuaciones(fase)

    elif opcion == "L":
        if not datos:
            print("Primero debes registrar datos.")
            continue

        fase = input("¿Qué fase quieres listar? (inicial / semifinal / final): ").lower()
        listarPuntuacionesEquipo(fase, datos, inicial, semifinal, final)

    elif opcion == "C":
        if not datos:
            print("Primero debes registrar datos.")
            continue

        fase = input("¿De qué fase quieres la clasificación?: ").lower()
        calculaClasificados(fase, datos, inicial, semifinal, final)

    elif opcion == "S":
        print("Saliendo...")

    else:
        print("Opción inválida.")
