# Clase base llamada materia que serán las que impartirá el maestro
class Materia:
    def __init__(self, nombre):
        self.nombre = nombre 
        self.horario = None
    
    def asignar_horario(self, dia, hora):
        """Asigna un horario específico a la materia."""
        self.horario = f"{dia} a las {hora}"
    
    def __str__(self):
        """Devuelve la representación en cadena de la materia."""
        return f"{self.nombre} - {self.horario if self.horario else 'Sin horario'}"


# Clases derivadas que representan tipos específicos de materias

class MateriaTeorica(Materia):
    def __init__(self, nombre, contenido_teorico):
        super().__init__(nombre)
        self.contenido_teorico = contenido_teorico
    
    def mostrar_contenido(self):
        """Muestra el contenido teórico de la materia."""
        return f"Contenido teórico de {self.nombre}: {self.contenido_teorico}"

    def __str__(self):
        """Modifica la representación en cadena para incluir el tipo de materia."""
        return f"{self.nombre} (Teórica) - {self.horario if self.horario else 'Sin horario'}"


class MateriaPractica(Materia):
    def __init__(self, nombre, equipo_necesario):
        super().__init__(nombre)
        self.equipo_necesario = equipo_necesario
    
    def mostrar_equipo(self):
        """Muestra el equipo necesario para la materia práctica."""
        return f"Equipo necesario para {self.nombre}: {self.equipo_necesario}"

    def __str__(self):
        """Modifica la representación en cadena para incluir el tipo de materia."""
        return f"{self.nombre} (Práctica) - {self.horario if self.horario else 'Sin horario'}"


# Clase base llamada maestro que representará al maestro y que materias se le asignarán
class Maestro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []

    def asignar_materia(self, materia):
        """Asigna una materia a un maestro."""
        self.materias.append(materia)
    
    def mostrar_info(self):
        """Muestra la información del maestro y las materias asignadas."""
        print(f"\n Maestro: {self.nombre}")
        for materia in self.materias:
            print(f"{materia}")


# Clases derivadas de la clase Maestro

class MaestroFullTime(Maestro):
    def __init__(self, nombre, horas_trabajadas):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
    
    def mostrar_info(self):
        """Muestra la información del maestro full-time, incluyendo las horas trabajadas."""
        super().mostrar_info()
        print(f"Horas trabajadas: {self.horas_trabajadas} horas a la semana")


class MaestroPartTime(Maestro):
    def __init__(self, nombre, horas_trabajadas):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
    
    def mostrar_info(self):
        """Muestra la información del maestro part-time, incluyendo las horas trabajadas."""
        super().mostrar_info()
        print(f"Horas trabajadas: {self.horas_trabajadas} horas a la semana")


# Gestión de horarios disponibles
horarios_disponibles = {
    "Lunes": ["8:00 AM", "10:00 AM", "2:00 PM"],
    "Martes": ["9:00 AM", "11:00 AM", "3:00 PM"],
}

# Creando objetos de maestros
m1 = MaestroFullTime("Profesor Juan", 40)
m2 = MaestroPartTime("Profesora Ana", 20)

# Creando objetos de materias
mat1 = MateriaTeorica("Matemáticas", "Cálculo, álgebra y geometría")
mat2 = MateriaPractica("Historia", "Computadora, proyector, y documentos históricos")
mat3 = MateriaTeorica("Física", "Mecánica clásica y electromagnetismo")

# Asignar materias a maestros
m1.asignar_materia(mat1)
m1.asignar_materia(mat2)

m2.asignar_materia(mat3)

# Asignar horarios a las materias
mat1.asignar_horario("Lunes", "8:00 AM")
mat2.asignar_horario("Martes", "9:00 AM")
mat3.asignar_horario("Lunes", "10:00 AM")

# Mostrar la información de los maestros
m1.mostrar_info()
m2.mostrar_info()

# Mostrar contenido específico de materias
print(mat1.mostrar_contenido())
print(mat2.mostrar_equipo())
