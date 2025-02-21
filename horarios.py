# Proyecto para autoasignación de horario dependiendo de disponibilidad de los maestros de una escuela
# Saúl Emmanuel De León Estrada

#Clase llamada materia que serán las que impartirá el maestro
class Materia:
    def __init__(self,nombre):
        self.nombre = nombre 
        self.horario = None
    
    def asignar_horario(self,dia,hora):
        self.horario = f"{dia} a las {hora}"

    
    def __str__(self):
        return f"{self.nombre} - {self.horario if self.horario else 'Sin horario'}"
    

# Clase llamada maestro que representará al maestro y que materias se le asignarán
class Maestro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []

    def asignar_materia(self,materia):
        self.materias.append(materia)

    
    def mostrar_info(self):
        print(f"\n Maestro: {self.nombre}")
        for materia in self.materias:
            print(f"{materia}")


#Gestioón de horarios disponibles
horarios_disponibles = {
    "Lunes": ["8:00 AM", "10:00 AM", "2:00 PM"],
    "Martes": ["9:00 AM", "11:00 AM", "3:00 PM"],
}       

# Creando objetos de maestros
m1 = Maestro("Profesor Juan")
m2 = Maestro("Profesora Ana")

#Creando objetos de materias
mat1 = Materia("Matemáticas")
mat2 = Materia("Historia")
mat3 = Materia("Física")

# Asignar materias a maestros
m1.asignar_materia(mat1)
m1.asignar_materia(mat2)

m2.asignar_materia(mat3)

# Asignar horarios a las materias
mat1.asignar_horario("Lunes", "8:00 AM")
mat2.asignar_horario("Martes", "9:00 AM")
mat3.asignar_horario("Lunes", "10:00 AM")

# Mostrar la información
m1.mostrar_info()
m2.mostrar_info()