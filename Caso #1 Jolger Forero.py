class SistemaCalificacion:
    def __init__(self):
        """Inicializa los contadores del sistema."""
        self.total_pedidos = 0
        self.puntuacion_total = 0
        self.pedidos_excelentes = 0

    def solicitar_calificacion(self):
        """Solicita la calificación del cliente para cada pedido."""
        while True:
            try:
                calificacion = int(input("Ingrese la calificación del pedido (1-5, o 0 para finalizar): "))
                if calificacion == 0:
                    return 0
                if 1 <= calificacion <= 5:
                    return calificacion
                else:
                    print("⚠️ Calificación inválida. Debe ser entre 1 y 5.")
            except ValueError:
                print("⚠️ Entrada inválida. Debe ingresar un número.")

    def procesar_pedidos(self):
        while True:
            calificacion = self.solicitar_calificacion()
            if calificacion == 0:
                break

            self.total_pedidos += 1
            self.puntuacion_total += calificacion

            if calificacion == 5:
                self.pedidos_excelentes += 1

        self.mostrar_resultados()

    def mostrar_resultados(self):
        print("\nRESULTADOS DEL SISTEMA DE CALIFICACIÓN")
        print("-----------------------------------------")

        if self.total_pedidos > 0:
            promedio = self.puntuacion_total / self.total_pedidos
            print(f"Total de pedidos procesados: {self.total_pedidos}")
            print(f"Promedio de satisfacción: {promedio:.2f}")
            print(f"Pedidos excelentes: {self.pedidos_excelentes}")
        else:
            print("No se procesaron pedidos.")


#zona de codigo principal
if __name__ == "__main__":
    sistema = SistemaCalificacion()
    sistema.procesar_pedidos()
