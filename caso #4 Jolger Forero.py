ESTADO_MALO = "D"
ESTADO_BUENO = "O"
SALIR = "STOP"

def revisar_unidad(estado, numero):
    if estado == ESTADO_MALO:
        return True, f"Unidad #{numero} con defecto"
    if estado == ESTADO_BUENO:
        return False, f"Unidad #{numero} aprobada"
    return False, f"Estado inválido en unidad #{numero}"

def obtener_porcentaje(fallas, total):
    if total == 0:
        return 0.0
    return (fallas / total) * 100

def control_produccion():
    total = 0
    defectuosas = 0
    lista_fallas = []
    lista_ok = []

    print("--- Control de Producción ---")
    print("D = Defectuosa | O = OK | STOP para terminar")

    lote = 0

    while True:
        lote += 1
        print(f"\nLote {lote}")

        entrada = input("Cantidad de unidades (o STOP): ").strip().upper()

        if entrada == SALIR:
            break

        try:
            cantidad = int(entrada)
            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
                lote -= 1
                continue
        except ValueError:
            print("Entrada no válida.")
            lote -= 1
            continue

        contador = 0
        while contador < cantidad:
            contador += 1
            estado = input(f"Unidad {contador}/{cantidad} (D/O): ").strip().upper()

            if estado not in (ESTADO_MALO, ESTADO_BUENO):
                print("Ingrese solo D u O.")
                contador -= 1
                continue

            es_mala, texto = revisar_unidad(estado, total + 1)
            total += 1

            if es_mala:
                defectuosas += 1
                lista_fallas.append(texto)
            else:
                lista_ok.append(texto)

    mostrar_reporte(defectuosas, total, lista_fallas, lista_ok)

def mostrar_reporte(defectuosas, total, fallas, ok):
    porcentaje = obtener_porcentaje(defectuosas, total)

    print("\n--- REPORTE FINAL ---")
    print(f"Unidades procesadas: {total}")
    print(f"Defectuosas: {defectuosas}")
    print(f"Porcentaje defectuoso: {porcentaje:.2f}%")

    print("\nUnidades defectuosas:")
    if fallas:
        for f in fallas:
            print(f"- {f}")
    else:
        print("Ninguna")

    print("\nUnidades aprobadas:")
    if ok:
        for o in ok:
            print(f"- {o}")
    else:
        print("Ninguna")

#zona de codigo principal

if __name__ == "__main__":
    control_produccion()
