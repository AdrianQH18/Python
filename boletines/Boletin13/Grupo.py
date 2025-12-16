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