from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self, nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"


class Alumno(Persona):
    def __init__(self, nombre, apellido,edad,ciclo,grupo=None):
        super().__init__(nombre, apellido)
        self.edad = edad
        self.ciclo = ciclo
        self.grupo = grupo
        self.mayor_edad=edad>=18

class Profesor(Persona):
    DEPARTAMENTO_VALIDOS={"Informatica","Empresa","Ingles"}

    def __init__(self,nombre,apellido,departamento,grupoTutor=None):
        if departamento not in self.DEPARTAMENTO_VALIDOS:
            raise ValueError("Departamento no valido")

        super().__init__(nombre,apellido)
        self.departamento = departamento
        self.grupoTutor = grupoTutor

class Modulo:
    def __init__(self,nombre,curso,horas_semanales,optativo):
        self.nombre=nombre
        self.curso=curso
        self.horas_semanales=horas_semanales
        self.optativo=optativo

class Ciclo:
    def __init__(self,nombre,grado):
        self.nombre=nombre
        self.grado=grado
        self.modulos=[]

    def anadir(self,modulo):
        self.modulos.append(modulo)

class Grupo:
    def __init__(self, nombre, ciclo, curso, tutor):
        self.nombre = nombre
        self.ciclo = ciclo
        self.curso = curso
        self.tutor = tutor
        self.alumnos = []

    def anadir_alumno(self, alumno):
        self.alumnos.append(alumno)
        alumno.grupo = self

    def eliminar_alumno(self, alumno):
        if alumno in self.alumnos:
            self.alumnos.remove(alumno)
            alumno.grupo = None
        else:
            print("⚠️ El alumno no pertenece a este grupo")

    def listar_info(self):
        print(f"📘 Grupo: {self.nombre}")
        print(f"Ciclo: {self.ciclo.nombre} ({self.ciclo.grado})")
        print(f"Curso: {self.curso}")
        print(f"Tutor: {self.tutor.nombre} {self.tutor.apellido}")
        print(f"Nº de alumnos: {len(self.alumnos)}")

        print("\n👩‍🎓 Alumnos:")
        for alumno in self.alumnos:
            estado = "Mayor de edad" if alumno.mayor_edad else "Menor de edad"
            print(f"- {alumno.nombre} {alumno.apellido} ({estado})")

        print("\n📚 Módulos del ciclo:")
        for modulo in self.ciclo.modulos:
            tipo = "Optativo" if modulo.optativo else "Obligatorio"
            print(
                f"- {modulo.nombre} | {modulo.curso} | "
                f"{modulo.horas_semanales}h | {tipo}"
            )

dam = Ciclo("Desarrollo de Aplicaciones Multiplataforma", "Superior")

dam.anadir(Modulo("Programación", "primero", 8, False))
dam.anadir(Modulo("Bases de Datos", "primero", 6, False))

prof = Profesor("Ana", "López", "Informatica")
grupo_dam1 = Grupo("DAM1", dam, "primero", prof)

al1 = Alumno("Carlos", "Pérez", 19, dam)
al2 = Alumno("Lucía", "Gómez", 17, dam)

grupo_dam1.anadir_alumno(al1)
grupo_dam1.anadir_alumno(al2)

grupo_dam1.listar_info()
