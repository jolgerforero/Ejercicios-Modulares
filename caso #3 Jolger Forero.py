SALDO_BASE = 1000.0

def registrar_deposito(saldo, valor):
    if valor <= 0:
        print("El valor debe ser mayor que cero.")
        return saldo, False

    saldo += valor
    print(f"Depósito exitoso: {valor:.2f}")
    return saldo, True

def registrar_retiro(saldo, valor):
    if valor <= 0:
        print("El valor debe ser mayor que cero.")
        return saldo, False

    if saldo >= valor:
        saldo -= valor
        print(f"Retiro exitoso: {valor:.2f}")
        return saldo, True
    else:
        print(f"Fondos insuficientes. Saldo disponible: {saldo:.2f}")
        return saldo, False

def gestionar_operaciones():
    saldo = SALDO_BASE
    operaciones_ok = 0

    print("--- Transacciones Bancarias ---")
    print(f"Saldo inicial: {saldo:.2f}")

    while True:
        opcion = input("\nIngrese 'D' para depósito, 'R' para retiro o 'FIN' para salir: ").strip().upper()

        if opcion == "FIN":
            break

        if opcion not in ("D", "R"):
            print("Opción inválida.")
            continue

        try:
            valor = float(input("Ingrese el monto: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        realizado = False

        if opcion == "D":
            saldo, realizado = registrar_deposito(saldo, valor)
        else:
            saldo, realizado = registrar_retiro(saldo, valor)

        if realizado:
            operaciones_ok += 1

    mostrar_resumen(saldo, operaciones_ok)

def mostrar_resumen(saldo_final, total):
    print("\n--- RESUMEN ---")
    print(f"Saldo final: {saldo_final:.2f}")
    print(f"Transacciones válidas: {total}")

#zona de codigo principal

if __name__ == "__main__":
    gestionar_operaciones()
