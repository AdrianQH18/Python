from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self, nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"