CODIGUIÑO = "1324"

def verificar_acceso(codigo_ingresado):
    
    return codigo_ingresado == CODIGUIÑO


def control_acceso_almacen():
    
    accesos_permitidos = 0
    accesos_denegados = 0
    registro_eventos = []

    print("ZONAS DE ALMACEN")
    print(f"Código de Acceso Requerido: {CODIGUIÑO}")
    print("Ingrese 'SALIR' para salir y ver resumen de accesos.")
    
    while True:
        codigo_empleado = input("\nIngrese código de acceso requerido: ").strip().upper()

        if codigo_empleado == "SALIR":
            break
        acceso_concedido = verificar_acceso(codigo_empleado)
        if acceso_concedido:
            accesos_permitidos += 1
            mensaje = f"Registro de acceso exitoso para código: {codigo_empleado}."
            print("Acceso CONCEDIDO.")
        else:
            accesos_denegados += 1
            mensaje = f"Intento fallido de acceso con código: {codigo_empleado}."
            print("Acceso DENEGADO. Código invalido.")
        
    
        registro_eventos.append(mensaje)

    
    mostrar_resultados(accesos_permitidos, accesos_denegados, registro_eventos)

def mostrar_resultados(permitidos, denegados, registro):
    print("\nRESUMEN")
    print(f"Total de Accesos Permitidos: {permitidos}")
    print(f"Total de Accesos Denegados: {denegados}")
    print(f"Totalidad de Intentos Procesados: {permitidos + denegados}")

    print("\nRESUMEN DETALLADO")
    if registro:
        for evento in registro:
            print(f"- {evento}")
    else:
        print("No hay registro de intentos de acceso.")

#Zona de odigo principal
if __name__ == "__main__":
    control_acceso_almacen()