EDAD_MIN = 25
EDAD_MAX = 45
SALIR = 0

def edad_valida(edad):
    return EDAD_MIN <= edad <= EDAD_MAX

def crear_registro(edad):
    return f"Participante registrado con {edad} años"

def iniciar_encuesta():
    total = 0
    en_objetivo = 0
    suma_edades = 0
    registros = []

    print("--- Encuesta de Mercado ---")
    print(f"Rango objetivo: {EDAD_MIN} a {EDAD_MAX} años")
    print(f"Ingrese {SALIR} para finalizar")

    while True:
        try:
            dato = input("\nEdad del participante: ").strip()
            edad = int(dato)

            if edad == SALIR:
                break

            if edad < 0:
                print("La edad no puede ser negativa.")
                continue

            total += 1
            suma_edades += edad

            if edad_valida(edad):
                en_objetivo += 1
                print("Dentro del público objetivo")
            else:
                print("Fuera del rango objetivo")

            registros.append(crear_registro(edad))

        except ValueError:
            print("Debe ingresar un número entero.")

    mostrar_resumen_encuesta(total, en_objetivo, suma_edades, registros)

def promedio_edad(suma, total):
    if total == 0:
        return 0.0
    return suma / total

def mostrar_resumen_encuesta(total, objetivo, suma, registros):
    promedio = promedio_edad(suma, total)

    print("\n--- RESUMEN FINAL ---")
    print(f"Participantes registrados: {total}")
    print(f"Público objetivo: {objetivo}")
    print(f"Suma de edades: {suma}")
    print(f"Edad promedio: {promedio:.2f}")

    print("\nRegistro de participantes:")
    if registros:
        for r in registros:
            print(f"- {r}")
    else:
        print("Sin registros")

#zona de codigo principal
if __name__ == "__main__":
    iniciar_encuesta()
