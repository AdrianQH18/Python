# Queremos implementar una clase para gestionar un juego de Pokemon con las siguientes
# características:
# - Los atributos base que manejaremos serán código, nombre y tipo
# - Sólo trabajaremos con pokemon de primera generación por lo que el código estará entre el
# 1 y el 151, ambos incluidos
# - Los posibles tipos son Normal, Agua, Fuego, Planta, Volador, Lucha, Veneno, Eléctrico,
# Tierra, Roca, Psíquico, Hielo, Bicho, Fantasma y Dragón.
# - Cada pokemon debe de ser de un tipo pero podría ser de dos. Nunca mas
# - No necesitamos setters (ya que un pokemon una vez creado no puede modificar sus
# características) pero si getters apropiados para todas ellas
# - Además, crearemos un metodo que se llame evolución que permitirá que un pokemon
# evolucione en otro diferente. Para ello si un pokemon puede evolucionar en otro debe de
# tener de alguna forma una referencia al pokemon en el que evoluciona

class Pokemon:
    def __init__(self,codigo,nombre,tipos,evolucion=None):
        TIPOS={"Normal", "Agua", "Fuego", "Planta", "Volador", "Lucha", "Veneno", "Eléctrico", "Tierra", "Roca", "Psíquico", "Hielo", "Bicho", "Fantasma","Dragón"}
        if not (1 <= codigo <= 151):
            raise ValueError("El código debe estar entre 1 y 151")
        if not (1<=len(tipos)<=2):
            raise ValueError("Un pokemon debe tener entre 1 o 2 tipos")
        for tipo in tipos:
            if tipo not in TIPOS:
                raise ValueError("TIpo no valido")
        self._codigo=codigo
        self._nombre=nombre
        self._tipos=tuple(tipos)
        self._evolucion=evolucion

    def get_codigo(self):
        return self._codigo

    def get_nombre(self):
        return self._nombre

    def get_tipos(self):
        return self._tipos

    def get_evolucion(self):
        return self._evolucion

    def evolucion(self):
        if self._evolucion is None:
            print(self._nombre,"no puede evolucionar")
        else:
            print(self._nombre,"evoluciona a ",self._evolucion.get_nombre())
            return self._evolucion

raichu = Pokemon(26, "Raichu", ["Eléctrico"])
pikachu = Pokemon(25, "Pikachu", ["Eléctrico"], raichu)
pichu = Pokemon(172 - 21, "Pichu", ["Eléctrico"], pikachu)  # código ajustado a 1ª gen

actual = pikachu
actual = actual.evolucion()