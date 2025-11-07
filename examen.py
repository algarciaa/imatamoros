while True:
    try:
        cantidad = int(input("Ingrese la cantidad de alumnos: "))
        if cantidad > 0:
            break
        else:
            print("Error: la cantidad debe ser un número positivo.")
    except ValueError:
        print("Error: ingrese un número entero válido.")


calificaciones = []

for i in range(cantidad):
    while True:
        try:
            nota = float(input(f"Ingrese la calificación del alumno {i + 1}: "))
            # Validación del rango
            if 0.0 <= nota <= 10.0:
                calificaciones.append(nota)
                break
            else:
                print("Error: la calificación debe estar entre 0.0 y 10.0.")
        except ValueError:
            print("Error: debe ingresar un número válido.")


suma_notas = sum(calificaciones)
promedio = suma_notas / cantidad

aprobados = 0
reprobados = 0

for nota in calificaciones:
    if nota >= 7.0:
        aprobados += 1
    else:
        reprobados += 1

