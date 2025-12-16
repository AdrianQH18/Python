from Trimestre1.Boletin13.Persona import Persona


class Profesor(Persona):
    DEPARTAMENTO_VALIDOS={"Informatica","Empresa","Ingles"}

    def __init__(self,nombre,apellido,departamento,grupoTutor=None):
        if departamento not in self.DEPARTAMENTO_VALIDOS:
            raise ValueError("Departamento no valido")

        super().__init__(nombre,apellido)
        self.departamento = departamento
        self.grupoTutor = grupoTutor