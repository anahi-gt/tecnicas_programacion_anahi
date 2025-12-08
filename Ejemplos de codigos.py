# ============================================
#        PROGRAMA PERSONALIZADO OOP
#      Autora: Anahí Jaela Grefa Tapuy
# ============================================

# ------------ CLASE BASE --------------------
class Persona:
    def __init__(self, nombre, apellido, genero, edad):
        self._apellido = apellido
        self._genero = genero
        self._edad = edad

    # Método común a todas las personas
    def mostrar_info(self):
        return f"{self._nombre} {self._apellido} ({self._genero}), {self._edad} años"


# ------------ CLASES DERIVADAS --------------------

# 1. Estudiante
class Estudiante(Persona):
    def __init__(self, nombre, apellido, genero, edad, carrera):
        super().__init__(nombre, apellido, genero, edad)
        self.carrera = carrera

    def mostrar_info(self):
        return (f"Estudiante: {self._nombre} {self._apellido} ({self._genero}), "
                f"{self._edad} años - Carrera: {self.carrera}")


# 2. Empleado
class Empleado(Persona):
    def __init__(self, nombre, apellido, genero, edad, puesto):
        super().__init__(nombre, apellido, genero, edad)
        self.puesto = puesto

    def mostrar_info(self):
        return (f"Empleado: {self._nombre} {self._apellido} ({self._genero}), "
                f"{self._edad} años - Puesto: {self.puesto}")


# 3. Paciente
class Paciente(Persona):
    def __init__(self, nombre, apellido, genero, edad, enfermedad):
        super().__init__(nombre, apellido, genero, edad)
        self.enfermedad = enfermedad

    def mostrar_info(self):
        return (f"Paciente: {self._nombre} {self._apellido} ({self._genero}), "
                f"{self._edad} años - Diagnóstico: {self.enfermedad}")


# 4. Gato (NO hereda de Persona)
class Gato:
    def __init__(self, nombre, color, edad):
        self.nombre = nombre
        self.color = color
        self.edad = edad

    def mostrar_info(self):
        return f"Gato: {self.nombre}, color {self.color}, edad {self.edad} años"


# ============================================
#          OBJETOS CON TUS DATOS
# ============================================

anahi_estudiante = Estudiante("Anahi Jaela", "Grefa Tapuy", "F", 22, "Tecnologías de la Información")
anahi_empleado   = Empleado("Anahi Jaela", "Grefa Tapuy", "F", 22, "Asistente Administrativa")
anahi_paciente   = Paciente("Anahi Jaela", "Grefa Tapuy", "F", 22, "Chequeo general")
mi_gato          = Gato("Mishito", "Blanco", 3)

# ============================================
#            IMPRIMIR RESULTADOS
# ============================================

print(anahi_estudiante.mostrar_info())
print(anahi_empleado.mostrar_info())
print(anahi_paciente.mostrar_info())
print(mi_gato.mostrar_info())
