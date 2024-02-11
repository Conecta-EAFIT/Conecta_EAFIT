def guardar_calificaciones(calificaciones):
    with open("calificaciones.txt", "w") as archivo:
        for calificacion in calificaciones:
            archivo.write(str(calificacion) + "\n")

def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        print("No se han ingresado calificaciones.")
    else:
        cal_prom = sum(calificaciones) / len(calificaciones)
        print("La calificación promedio es:", cal_prom)

calificaciones = []

while True:
    x = input("¿Desea calificar a este profesor? (Y/N): ")
    if x.lower() == "y":
        calificacion = int(input("Ingrese un número entre 1 y 5: "))
        if calificacion < 1 or calificacion > 5:
            print("Error: La calificación debe estar entre 1 y 5.")
        else:
            calificaciones.append(calificacion)
    else:
        guardar_calificaciones(calificaciones)
        calcular_promedio(calificaciones)
        break
