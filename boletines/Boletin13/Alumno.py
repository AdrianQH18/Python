from Trimestre1.Boletin13.Persona import Persona


class Alumno(Persona):
    def __init__(self, nombre, apellido,edad,ciclo,grupo):
        super().__init__(nombre, apellido)
        self.edad = edad
        self.ciclo = ciclo
        self.grupo = grupo
        self.mayor_edad=edad>=18