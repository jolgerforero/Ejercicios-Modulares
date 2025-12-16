LIMITE_CRITICO = 90.0

def es_uso_alto(uso):
    return uso > LIMITE_CRITICO

def vigilar_servidor():
    alertas = 0
    mediciones = 0
    historial = []

    print("--- Monitoreo de CPU ---")
    print(f"Límite crítico: {LIMITE_CRITICO:.1f}%")
    print("Ingrese un número negativo para finalizar.")

    while True:
        try:
            dato = input("\nUso de CPU (%): ").strip()
            uso = float(dato)

            if uso < 0:
                break

            if uso > 100:
                print("El valor no puede superar 100.")
                continue

            mediciones += 1

            if es_uso_alto(uso):
                alertas += 1
                aviso = f"Alerta crítica: {uso:.1f}% (Medición {mediciones})"
                historial.append(aviso)
                print("Alerta registrada")
            else:
                print(f"Uso normal: {uso:.1f}%")

        except ValueError:
            print("Debe ingresar un número válido.")

    mostrar_resumen_monitoreo(mediciones, alertas, historial)

def mostrar_resumen_monitoreo(total, alertas, historial):
    print("\n--- RESUMEN DEL MONITOREO ---")
    print(f"Total de mediciones: {total}")
    print(f"Alertas críticas (uso > {LIMITE_CRITICO:.1f}%): {alertas}")

    print("\nHistorial de alertas:")
    if historial:
        for h in historial:
            print(f"- {h}")
    else:
        print("No se detectaron alertas críticas.")

#zona de codigo principal
if __name__ == "__main__":
    vigilar_servidor()
