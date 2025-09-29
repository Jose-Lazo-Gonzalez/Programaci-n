asistencias=float(input("cual es tu porcentaje de asistencias?:"))
nota= float(input("cual es tu nota en el examen final?:"))
if asistencias>=80 and nota>=6:
    print("has aprobado!")
else:
    print("has suspendido :( )")
print("desconectando...")