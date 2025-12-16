STOCK_BASE = 50
LIMITE_REPOSICION = 10
SALIDA = -1

def registrar_venta(stock, cantidad):
    if cantidad <= 0:
        return stock, False, "La cantidad debe ser mayor que cero."

    if stock >= cantidad:
        stock -= cantidad
        return stock, True, f"Venta realizada: {cantidad} unidades. Stock actual: {stock}"
    else:
        return stock, False, f"Venta cancelada: solo hay {stock} unidades disponibles."

def requiere_reposicion(stock):
    return stock <= LIMITE_REPOSICION

def gestionar_inventario():
    stock = STOCK_BASE
    ventas_ok = 0
    aviso = None

    print("--- Gestión de Inventario ---")
    print(f"Stock inicial: {stock}")
    print(f"Punto de reposición: {LIMITE_REPOSICION}")
    print(f"Ingrese {SALIDA} para finalizar")

    while True:
        try:
            dato = input("\nCantidad vendida: ").strip()
            cantidad = int(dato)

            if cantidad == SALIDA:
                print("\nProceso finalizado por el usuario.")
                break

            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue

        except ValueError:
            print("Debe ingresar un número entero.")
            continue

        stock_nuevo, valido, mensaje = registrar_venta(stock, cantidad)
        print(mensaje)

        if valido:
            stock = stock_nuevo
            ventas_ok += 1

        if valido and requiere_reposicion(stock):
            aviso = f"ALERTA: Stock bajo ({stock} unidades). Reposición necesaria."
            print("\n" + aviso)
            break

    mostrar_resumen_inventario(STOCK_BASE, stock, ventas_ok, aviso)

def mostrar_resumen_inventario(inicial, final, ventas, aviso):
    print("\n--- RESUMEN FINAL ---")
    print(f"Stock inicial: {inicial}")
    print(f"Ventas procesadas: {ventas}")
    print(f"Stock final: {final}")

    print("\nEstado de reposición:")
    if aviso:
        print(aviso)
    else:
        print(f"Stock suficiente, mayor a {LIMITE_REPOSICION} unidades.")

#zona de codigo principal
if __name__ == "__main__":
    gestionar_inventario()
