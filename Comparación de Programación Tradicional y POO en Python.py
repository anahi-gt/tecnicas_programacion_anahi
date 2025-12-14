# Comparación de Programación Tradicional y Programación Orientada a Objetos (POO)
# Cálculo del promedio semanal del clima

dias_semana = [
    "Lunes", "Martes", "Miércoles",
    "Jueves", "Viernes", "Sábado", "Domingo"
]


# PROGRAMACIÓN TRADICIONAL


def ingresar_temperaturas_tradicional():
    temperaturas = []

    for dia in dias_semana:
        temp = float(input(f"Ingrese la temperatura del {dia}: "))
        temperaturas.append(temp)

    return temperaturas


def calcular_promedio_tradicional(temperaturas):
    return sum(temperaturas) / len(temperaturas)


def ejecutar_tradicional():
    print("\n--- Programación Tradicional ---")
    temperaturas = ingresar_temperaturas_tradicional()
    promedio = calcular_promedio_tradicional(temperaturas)
    print(f"Promedio semanal (Tradicional): {promedio:.2f}°C")



# PROGRAMACIÓN ORIENTADA A OBJETOS


class ClimaSemanal:
    def __init__(self):
        self.temperaturas = {}

    def ingresar_temperaturas(self):
        for dia in dias_semana:
            temp = float(input(f"Ingrese la temperatura del {dia}: "))
            self.temperaturas[dia] = temp

    def calcular_promedio(self):
        return sum(self.temperaturas.values()) / len(self.temperaturas)


def ejecutar_poo():
    print("\n--- Programación Orientada a Objetos (POO) ---")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"Promedio semanal (POO): {promedio:.2f}°C")



# FUNCIÓN PRINCIPAL


def main():
    ejecutar_tradicional()
    ejecutar_poo()


if __name__ == "__main__":
    main()