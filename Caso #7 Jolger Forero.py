META_OBJETIVO = 5000.0

def cumple_objetivo(monto):
    return monto >= META_OBJETIVO

def crear_mensaje(monto, numero):
    return f"¡Buen trabajo! Vendedor #{numero} alcanzó {monto:.2f}"

def revisar_ventas():
    total = 0
    exitosos = 0
    mensajes = []

    print("--- Control de Metas de Ventas ---")
    print(f"Meta establecida: ${META_OBJETIVO:.2f}")
    print("Ingrese un valor menor o igual a 0 para finalizar.")

    while True:
        try:
            dato = input("\nMonto de ventas: ").strip()
            monto = float(dato)

            if monto <= 0:
                break

            total += 1

            if cumple_objetivo(monto):
                exitosos += 1
                mensajes.append(crear_mensaje(monto, total))
                print("Meta alcanzada.")
            else:
                print("Meta no alcanzada.")

        except ValueError:
            print("Entrada inválida.")

    mostrar_resumen_ventas(total, exitosos, mensajes)

def mostrar_resumen_ventas(total, exitosos, mensajes):
    print("\n--- RESUMEN FINAL ---")
    print(f"Vendedores evaluados: {total}")
    print(f"Metas cumplidas: {exitosos}")

    print("\nFelicitaciones registradas:")
    if mensajes:
        for m in mensajes:
            print(f"- {m}")
    else:
        print("No hubo vendedores que cumplieran la meta.")

#zona de codigo principal
if __name__ == "__main__":
    revisar_ventas()
