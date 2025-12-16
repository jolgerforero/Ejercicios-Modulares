FINALIZAR = "FIN"
LIMITE_DESCUENTO_ALTO = 1000.0
LIMITE_DESCUENTO_BAJO = 500.0
DESCUENTO_ALTO = 0.10
DESCUENTO_BAJO = 0.05

def obtener_subtotal(precio, cantidad):
    return precio * cantidad

def evaluar_descuento(total):
    rebaja = 0.0
    porcentaje = 0.0
    detalle = "No aplica descuento por volumen."

    if total > LIMITE_DESCUENTO_ALTO:
        rebaja = total * DESCUENTO_ALTO
        porcentaje = DESCUENTO_ALTO
        detalle = f"Descuento del 10% aplicado (total mayor a ${LIMITE_DESCUENTO_ALTO:.2f})."
    elif total > LIMITE_DESCUENTO_BAJO:
        rebaja = total * DESCUENTO_BAJO
        porcentaje = DESCUENTO_BAJO
        detalle = f"Descuento del 5% aplicado (total mayor a ${LIMITE_DESCUENTO_BAJO:.2f})."

    return rebaja, porcentaje, detalle

def procesar_compra():
    total_compra = 0.0
    contador_items = 0

    print("--- Cálculo de Descuento por Compra ---")
    print("Escriba 'FIN' para terminar.")

    while True:
        try:
            precio_txt = input(f"\nProducto {contador_items + 1} - Precio: ").strip().upper()
            if precio_txt == FINALIZAR:
                break

            precio = float(precio_txt)
            if precio <= 0:
                print("El precio debe ser mayor que cero.")
                continue

            cantidad_txt = input(f"Producto {contador_items + 1} - Cantidad: ").strip().upper()
            if cantidad_txt == FINALIZAR:
                break

            cantidad = int(cantidad_txt)
            if cantidad <= 0:
                print("La cantidad debe ser positiva.")
                continue

            total_compra += obtener_subtotal(precio, cantidad)
            contador_items += 1
            print(f"Total acumulado: ${total_compra:.2f}")

        except ValueError:
            print("Entrada incorrecta. Intente de nuevo.")

    if contador_items == 0:
        print("\nNo se registraron productos.")
        return

    descuento, _, info = evaluar_descuento(total_compra)
    total_pagar = total_compra - descuento
    mostrar_resumen(total_compra, descuento, total_pagar, info)

def mostrar_resumen(subtotal, descuento, total, info):
    print("\n--- RESUMEN FINAL ---")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}")
    print("\nDetalle del descuento:")
    print(info)

#zona de codigo principal
if __name__ == "__main__":
    procesar_compra()
