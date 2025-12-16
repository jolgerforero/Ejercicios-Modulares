LIMITE_HORAS = 5
PAGO_ALTO = 15.0
PAGO_BAJO = 10.0
SALIR = -1

def obtener_tarifa(horas):
    if horas > LIMITE_HORAS:
        return PAGO_ALTO
    return PAGO_BAJO

def calcular_pago_extra(horas):
    return horas * obtener_tarifa(horas)

def procesar_nomina():
    total_pago = 0.0
    empleados_pagados = 0

    print("--- Bonificaciones por Horas Extra ---")
    print(f"Pago alto: ${PAGO_ALTO:.2f} | Pago bajo: ${PAGO_BAJO:.2f}")
    print(f"Ingrese {SALIR} para finalizar")

    while True:
        try:
            dato = input("\nHoras extra trabajadas: ").strip()
            horas = int(dato)

            if horas < 0:
                break

            if horas == 0:
                print("Sin bonificación para 0 horas.")
                continue

        except ValueError:
            print("Debe ingresar un número entero.")
            continue

        pago = calcular_pago_extra(horas)
        total_pago += pago
        empleados_pagados += 1

        print(f"Bonificación asignada: ${pago:.2f}")

    mostrar_resumen_nomina(total_pago, empleados_pagados)

def mostrar_resumen_nomina(total, empleados):
    print("\n--- RESUMEN FINAL ---")
    print(f"Empleados bonificados: {empleados}")
    print(f"Total pagado en bonificaciones: ${total:.2f}")

#zona de codigo principal
if __name__ == "__main__":
    procesar_nomina()
