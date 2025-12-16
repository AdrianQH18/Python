# Queremos implementar una clase para gestionar una aplicación de gestión de notas. Cada
# nota tendrá cuatro elementos: título, descripción, color (debe de se amarillo, verde, blanco o
# cyan para una futura implementación en un entorno gráfico) y fecha de creación.
# Necesitamos, además, añadir los siguientes métodos: crearNota, eliminarNota y listarNota
# No hace falta que hagas entradas por teclado: crea los métodos y pruébalos llamándolos
# directamente.
# Trata de que la visualización de la nota sea lo mas agradable posible en pantalla usando
# fstrings
class Notas:
    colores_validos={"amarrillo","verde","blanco","cyan"}
    def __init__(self):
        self.notas=[]

    def crearNota(self,titulo,descripcion,color,fechaCreacion):
        if color not in self.colores_validos:
            print("Color invalido")
            return
        nota = {
            "titulo": titulo,
            "descripcion": descripcion,
            "color": color,
            "fecha": fechaCreacion
        }
        self.notas.append(nota)
        print(f"nota: {titulo} creada")

    def eliminarNota(self, titulo):
        for nota in self.notas:
            if nota["titulo"] == titulo:
                self.notas.remove(nota)
                print(f"🗑️ Nota '{titulo}' eliminada")
                return
        print(f"⚠️ No existe la nota '{titulo}'")

    def listarNota(self):
        if not self.notas:
            print("📭 No hay notas")
            return

        for nota in self.notas:
            print(
                f"📌 {nota['titulo']}\n"
                f"📝 {nota['descripcion']}\n"
                f"🎨 Color: {nota['color']}\n"
                f"📅 Fecha: {nota['fecha']}\n"
                f"{'-' * 30}"
            )
app = Notas()

app.crearNota("Compra", "Comprar pan", "amarillo", "16/12/2025")
app.crearNota("Estudio", "Repasar Python", "verde", "16/12/2025")

app.listarNota()

app.eliminarNota("Compra")
app.listarNota()
